# Telegram Userbot (Telethon + Render)

A simple Telegram userbot using Telethon, deployable on Render.

## 🚀 Features
- Replies to `!ping` with `pong ✅`
- Runs 24/7 on Render (Free Tier)

---

## 🔧 Setup

### 1. Get Telegram API Keys
- Visit [https://my.telegram.org](https://my.telegram.org)
- Create an app → copy **API_ID** and **API_HASH**

### 2. Generate Session String
Run locally:
```bash
pip install telethon
```

```python
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = int(input("Enter API ID: "))
api_hash = input("Enter API HASH: ")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Your SESSION STRING:")
    print(client.session.save())
```

Copy the session string (keep it secret).

### 3. Deploy on Render
- Fork this repo  
- Go to [Render Dashboard](https://dashboard.render.com/) → **New → Web Service**  
- Connect your GitHub repo  
- Add Environment Variables:
  - `API_ID`
  - `API_HASH`
  - `SESSION`
- Deploy 🚀

### 4. Test
- Send `!ping` in any chat with your account  
- Bot replies with `pong ✅`
