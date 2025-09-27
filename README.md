# 🚀 Telegram Userbot (Docker + Render + CI/CD)

A stable Telethon-based userbot with plugin system. Deployable via **Docker**, **docker-compose**, and **Render**.

---

## 🛠 Features
- Plugin loader (`plugins/` folder)
- Stable curated plugins:
  - Core: `!ping`, `!alive`, `!id`, `!help`
  - Fun: `!joke`, `!quote`
  - Admin: `!kick`, `!ban`, `!mute`, `!unmute`, `!promote`, `!demote`, `!purge`
  - Utility: `!calc`, `!wiki`, `!weather`, `!time`, `!note`
  - Extras: `!tags`, `!broadcast`, `!remind`, `!lock`
- CI/CD with GitHub Actions → auto-build Docker images

---

## 🔑 Generate Session String
Before deploying, you need a valid **SESSION STRING**.

1. Run the generator locally:
   ```bash
   pip install telethon
   python session_gen.py
   ```
2. Enter your **API_ID** and **API_HASH** (from [my.telegram.org](https://my.telegram.org)).  
3. Login with your phone number and OTP.  
4. Copy the generated **SESSION STRING**.  
5. Paste it in Render → Environment Variables → `SESSION`.

---

## ☁️ One-Click Deploy to Render

Click below to deploy instantly on Render:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

---

## 🔧 Run with Docker
```bash
docker build -t telegram-userbot .
docker run -d --name userbot   -e API_ID=12345   -e API_HASH=your_api_hash   -e SESSION=your_session_string   -e OWNER_ID=your_numeric_id   telegram-userbot
```

## 🔧 Run with docker-compose
```bash
docker-compose up -d
docker-compose down
```

## 🔄 CI/CD (GitHub Actions)
- Every push to **main** builds & pushes a Docker image → `ghcr.io/<username>/telegram-userbot:latest`
