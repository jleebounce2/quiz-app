#!/usr/bin/env python3
"""
Create schema in Neon PostgreSQL
"""

from psycopg2 import connect

NEON_URL = 'postgresql://neondb_owner:npg_X8N6kQFSmcBa@ep-wandering-brook-adu1zeum-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require'

def create_schema():
    print("🏗️ Creating schema in Neon PostgreSQL...")
    
    conn = connect(NEON_URL)
    cur = conn.cursor()
    
    try:
        # Read schema.sql
        with open('/Users/abc/.openclaw/workspace/quiz-app/schema.sql', 'r') as f:
            schema_sql = f.read()
        
        # Execute schema
        cur.execute(schema_sql)
        conn.commit()
        
        print("✅ Schema created successfully!")
        print("\n📊 Tables created:")
        print("   - members")
        print("   - xp_log")
        print("   - quizzes")
        print("   - quiz_attempts")
        print("   - indexes for performance")
        
    except Exception as e:
        conn.rollback()
        print(f"\n❌ Schema creation failed: {e}")
        raise
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    create_schema()
