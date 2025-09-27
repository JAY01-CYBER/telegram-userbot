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

## ☁️ Deploy on Render
- Use `render.yaml`
- Add environment variables: `API_ID`, `API_HASH`, `SESSION`, `OWNER_ID`

## 🔄 CI/CD (GitHub Actions)
- Every push to **main** builds & pushes a Docker image → `ghcr.io/<username>/telegram-userbot:latest`
