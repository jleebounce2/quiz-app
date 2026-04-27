# 🚀 Quiz App Migration Guide

## Project Created ✅
- **Name:** gamification-quiz
- **ID:** prj_0XueRQl9DiNsIjDp0mItqGK46HH7
- **Owner:** jleebounce-2720 (team_mS12nddTIC7q8ag7vPkmKzHw)

---

## 📋 Next Steps (Manual - 5 minutes)

### Step 1: Create Vercel Postgres Database

1. Go to **Vercel Dashboard**: https://vercel.com/dashboard
2. Select project: **gamification-quiz**
3. Go to **Storage** tab
4. Click **"Add Database"** → **"Create Database"**
5. Name: `gamification-db`
6. Click **"Create"**

### Step 2: Run Migration SQL

1. After database is created, click on it
2. Go to **"SQL"** tab
3. Copy the contents of `migrate-to-vercel.sql`
4. Paste into SQL editor
5. Click **"Run"**

### Step 3: Get Database Connection String

1. In the database page, click **"Connect"**
2. Copy the **Connection String** (looks like `postgres://user:pass@host/db`)
3. Or copy the individual env vars:
   - `POSTGRES_PRISMA_URL`
   - `POSTGRES_URL_NON_POOLING`

### Step 4: Add Environment Variables

1. Go to project **Settings** → **Environment Variables**
2. Add these variables:
   ```
   POSTGRES_URL=postgres://...
   POSTGRES_USER=your_user
   POSTGRES_PASSWORD=your_password
   POSTGRES_HOST=your_host
   POSTGRES_DATABASE=gamification-db
   ```
3. Click **"Save"**

### Step 5: Deploy the App

From your terminal:

```bash
cd /Users/abc/.openclaw/workspace/quiz-app
vercel --prod
```

---

## 📁 Files Ready

| File | Purpose |
|------|---------|
| `migrate-to-vercel.sql` | Complete database migration (schema + data) |
| `schema.sql` | Database schema only |
| `api/index.py` | Vercel serverless function (needs finalization) |
| `vercel.json` | Vercel deployment config |
| `templates/*.html` | Frontend templates (ready) |

---

## 🔄 Alternative: Keep It Simple

If Vercel Postgres setup is too complex right now, we can:

1. **Use Neon** (neon.tech) - easier setup
2. **Keep SQLite locally** - deploy quiz app as-is to Vercel with a different DB

Let me know which path you prefer!

---

## 🎯 Current Status

- ✅ Vercel project created
- ✅ Migration SQL prepared (all data exported)
- ⏳ Database needs to be created (via dashboard)
- ⏳ App needs deployment config finalized

**Time to complete:** ~10 minutes
