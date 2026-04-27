#!/usr/bin/env python3
"""
Migrate SQLite gamification data to Neon PostgreSQL
"""

import sqlite3
import json
from psycopg2 import connect, sql

# SQLite source
SQLITE_DB = '/Users/abc/.openclaw/workspace/trello-gamification.db'

# Neon PostgreSQL destination
NEON_URL = 'postgresql://neondb_owner:npg_X8N6kQFSmcBa@ep-wandering-brook-adu1zeum-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require'

def migrate():
    print("🔄 Starting migration from SQLite to Neon PostgreSQL...")
    
    # Connect to SQLite
    sqlite_conn = sqlite3.connect(SQLITE_DB)
    sqlite_conn.row_factory = sqlite3.Row
    sqlite_cur = sqlite_conn.cursor()
    
    # Connect to Neon
    neon_conn = connect(NEON_URL)
    neon_cur = neon_conn.cursor()
    
    try:
        # 1. Migrate Members
        print("\n📋 Migrating members...")
        sqlite_cur.execute("SELECT * FROM members")
        members = sqlite_cur.fetchall()
        
        for member in members:
            neon_cur.execute("""
                INSERT INTO members (name, total_xp, cards_done, badges, last_updated)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (name) DO UPDATE SET
                    total_xp = EXCLUDED.total_xp,
                    cards_done = EXCLUDED.cards_done,
                    badges = EXCLUDED.badges,
                    last_updated = EXCLUDED.last_updated
            """, (
                member['name'],
                member['total_xp'],
                member['cards_done'],
                member['badges'],  # Already JSON string
                member['last_updated']
            ))
        print(f"   ✅ Migrated {len(members)} members")
        
        # 2. Migrate XP Log
        print("\n📊 Migrating XP log...")
        sqlite_cur.execute("SELECT * FROM xp_log")
        xp_logs = sqlite_cur.fetchall()
        
        for log in xp_logs:
            neon_cur.execute("""
                INSERT INTO xp_log (member_name, xp_change, reason, card_id, card_name, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                log['member_name'],
                log['xp_change'],
                log['reason'],
                log['card_id'],
                log['card_name'],
                log['timestamp']
            ))
        print(f"   ✅ Migrated {len(xp_logs)} XP log entries")
        
        # 3. Migrate Quizzes
        print("\n🧠 Migrating quizzes...")
        sqlite_cur.execute("SELECT * FROM quizzes")
        quizzes = sqlite_cur.fetchall()
        
        for quiz in quizzes:
            neon_cur.execute("""
                INSERT INTO quizzes (id, question, options, correct_answer, category, xp_reward, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (
                quiz['id'],
                quiz['question'],
                quiz['options'],  # Already JSON string
                quiz['correct_answer'],
                quiz['category'],
                quiz['xp_reward'],
                quiz['created_at']
            ))
        print(f"   ✅ Migrated {len(quizzes)} quizzes")
        
        # 4. Migrate Quiz Attempts
        print("\n📝 Migrating quiz attempts...")
        sqlite_cur.execute("SELECT * FROM quiz_attempts")
        attempts = sqlite_cur.fetchall()
        
        for attempt in attempts:
            # SQLite stores boolean as 0/1, need to convert to Python bool
            is_correct = bool(attempt['correct'])
            neon_cur.execute("""
                INSERT INTO quiz_attempts (member_name, quiz_id, answer, correct, xp_awarded, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                attempt['member_name'],
                attempt['quiz_id'],
                attempt['answer'],
                is_correct,
                attempt['xp_awarded'],
                attempt['timestamp']
            ))
        print(f"   ✅ Migrated {len(attempts)} quiz attempts")
        
        # Commit all changes
        neon_conn.commit()
        
        print("\n✅ Migration complete!")
        print("\n📊 Summary:")
        print(f"   - Members: {len(members)}")
        print(f"   - XP Log Entries: {len(xp_logs)}")
        print(f"   - Quizzes: {len(quizzes)}")
        print(f"   - Quiz Attempts: {len(attempts)}")
        
    except Exception as e:
        neon_conn.rollback()
        print(f"\n❌ Migration failed: {e}")
        raise
    finally:
        sqlite_conn.close()
        neon_conn.close()

if __name__ == '__main__':
    migrate()
