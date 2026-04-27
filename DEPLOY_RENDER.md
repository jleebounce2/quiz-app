# Deploy Quiz App to Render.com 🚀

**Time:** 2 minutes  
**Cost:** Free tier

---

## 🎯 One-Click Deploy

### Option 1: Deploy from GitHub (Recommended)

1. **Push quiz-app to GitHub:**
   ```bash
   cd /Users/abc/.openclaw/workspace/quiz-app
   git init
   git add .
   git commit -m "Initial commit - Trello Quiz App"
   git remote add origin https://github.com/YOUR_USERNAME/trello-quiz-app.git
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to: https://render.com
   - Click **"New +"** → **"Web Service"**
   - Connect your GitHub account
   - Select the `trello-quiz-app` repository
   - Render will auto-detect `render.yaml` configuration
   - Click **"Create Web Service"**

3. **Add Database URL:**
   - In Render dashboard, go to **Environment** tab
   - Add variable: `NEON_DATABASE_URL`
   - Value: `postgresql://neondb_owner:npg_X8N6kQFSmcBa@ep-wandering-brook-adu1zeum-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require`
   - Click **"Save Changes"**

4. **Done!** Render will deploy and give you a URL like:
   ```
   https://trello-quiz-app-xyz.onrender.com
   ```

---

### Option 2: Deploy from Blueprint URL

If you don't want to use GitHub:

1. **Create a public gist or repo** with the quiz-app files
2. **Go to Render:** https://render.com
3. **Click "New +"** → **"Web Service"**
4. **Select "Deploy from blueprint URL"**
5. **Paste the URL** to your `render.yaml` file
6. **Add the NEON_DATABASE_URL** environment variable
7. **Click "Create Web Service"**

---

## 📊 Render Free Tier

- ✅ **512 MB RAM**
- ✅ **Shared CPU**
- ✅ **Automatic HTTPS**
- ✅ **Auto-deploy from Git**
- ✅ **750 hours/month free** (enough for 1 service running 24/7)

**Note:** Free services spin down after 15 min of inactivity. First request after spin-down takes ~30 seconds to wake up.

---

## 🔧 Manual Deployment (No Git)

If you want to deploy without Git:

1. **Zip the quiz-app folder:**
   ```bash
   cd /Users/abc/.openclaw/workspace
   zip -r quiz-app.zip quiz-app/
   ```

2. **Upload to Render:**
   - Go to https://render.com
   - Create new **Web Service**
   - Choose **"Deploy from uploaded files"**
   - Upload `quiz-app.zip`
   - Configure as above

---

## ✅ Verify Deployment

Once deployed, test the app:

1. Open your Render URL in browser
2. Select a member (Jason, Edward, etc.)
3. Take a quiz
4. Check leaderboard shows updated XP

---

## 🐛 Troubleshooting

### App won't start
Check **Logs** tab in Render dashboard for errors.

### Database connection failed
Verify `NEON_DATABASE_URL` environment variable is set correctly.

### Templates not loading
Render supports Flask + Jinja2 natively - this should work automatically.

### Slow first load
Free tier services spin down. First request triggers a cold start (~30s). Subsequent requests are fast.

---

## 📱 Share with Team

Once deployed, share the URL with your team:
- Edward
- Gourav
- Ibitola
- Olabode

They can start taking quizzes immediately!

---

**Ready to deploy?** Just follow Option 1 above! 🦞
