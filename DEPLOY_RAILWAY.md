# Deploy Quiz App to Railway 🚀

**Time:** 2 minutes  
**Cost:** Free tier ($5 credit/month)

---

## 🎯 Quick Deploy (2 Options)

### Option 1: Deploy from GitHub (Recommended - 2 min)

#### Step 1: Push to GitHub

```bash
cd /Users/abc/.openclaw/workspace/quiz-app

# Initialize git repo (if not already done)
git init
git add .
git commit -m "Trello Quiz App - Ready for Railway"

# Create repo on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/trello-quiz-app.git
git push -u origin main
```

#### Step 2: Deploy on Railway

1. **Go to:** https://railway.app
2. **Click:** "New Project"
3. **Select:** "Deploy from GitHub repo"
4. **Choose:** Your `trello-quiz-app` repository
5. **Railway auto-detects:** Python + nixpacks.toml
6. **Click:** "Deploy"

#### Step 3: Add Environment Variable

In Railway dashboard:
1. Click on your project
2. Go to **"Variables"** tab
3. Click **"New Variable"**
4. Add:
   - **Key:** `NEON_DATABASE_URL`
   - **Value:** `postgresql://neondb_owner:npg_X8N6kQFSmcBa@ep-wandering-brook-adu1zeum-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require`
5. Click **"Save"**

#### Step 4: Done! 🎉

Railway will redeploy automatically. Your URL will be:
```
https://trello-quiz-app-production.up.railway.app
```

---

### Option 2: Deploy from Folder (No Git - 3 min)

1. **Zip the folder:**
   ```bash
   cd /Users/abc/.openclaw/workspace
   zip -r quiz-app-deploy.zip quiz-app/
   ```

2. **Go to Railway:** https://railway.app
3. **Click:** "New Project"
4. **Select:** "Deploy from folder"
5. **Upload:** `quiz-app-deploy.zip`
6. **Add the `NEON_DATABASE_URL`** environment variable (same as above)
7. **Click:** "Deploy"

---

## 📊 Railway Free Tier

- ✅ **$5 credit/month** (enough for ~500 hours)
- ✅ **512 MB RAM**
- ✅ **Shared CPU**
- ✅ **Automatic HTTPS**
- ✅ **Auto-deploy from Git**
- ✅ **No credit card required**

**Note:** Unlike Render, Railway doesn't spin down services. Your app stays running 24/7!

---

## ✅ Verify Deployment

Once deployed:

1. **Open your Railway URL** in browser
2. **Select a member** (Jason, Edward, Gourav, Ibitola, Olabode)
3. **Take a quiz**
4. **Check leaderboard** - XP should update in real-time

---

## 🔧 What Railway Auto-Detects

Railway uses **Nixpacks** to build your app:

- ✅ Reads `nixpacks.toml` → Knows it's Python 3.12
- ✅ Reads `requirements.txt` → Installs Flask, psycopg2, gunicorn
- ✅ Reads `railway.json` → Knows to start with gunicorn
- ✅ Exposes `$PORT` automatically
- ✅ Handles SSL/HTTPS automatically

---

## 📱 Share with Team

Once live, share the URL:
- Edward
- Gourav  
- Ibitola
- Olabode

They can start earning XP immediately!

---

## 🐛 Troubleshooting

### Build fails
Check **Deployments** tab → Click failed deployment → View logs

### Database connection error
Verify `NEON_DATABASE_URL` is set correctly in Variables tab

### App won't start
Check logs for gunicorn errors. Make sure `app:app` is correct (Flask app object).

### Slow first load
Railway doesn't spin down, so this shouldn't happen. If it does, check logs.

---

## 🎯 Ready to Deploy?

**Fastest path:**
1. Push quiz-app to GitHub (1 min)
2. Connect Railway to GitHub repo (30 sec)
3. Add NEON_DATABASE_URL (30 sec)
4. Done! (1 min for deploy)

**Total time:** ~3 minutes

Let's do this! 🦞
