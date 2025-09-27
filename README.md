# Stable Telegram Userbot Plugin Pack

This is a curated pack of **stable** plugins for a Telethon-based userbot.
Drop these files into your project (use the provided `main.py` which loads plugins from `plugins/`).

## Included Plugins (stable-focused)
- ping: simple ping/pong
- alive: check bot status
- help: list commands
- id: get user id
- fun: jokes & quotes
- wiki: quick wikipedia lookup
- weather: uses wttr.in to fetch simple weather
- calc: safe calculator (using ast)
- time: show current time
- notes: save and get notes (file-based)
- tags: tag all members in a group (caution with large groups)
- admin: kick/ban/mute/unmute/promote/demote/purge (admin-only)
- anti_spam: basic flood detection and warn
- broadcast: send message to saved chats (OWNER only)
- remind: simple reminders persisted to a json file
- lock: lock/unlock sending messages in a chat (admin-only)

## Deploy
1. Create a repo and add these files.
2. On Render, set environment variables: API_ID, API_HASH, SESSION, OWNER_ID (your Telegram numeric ID).
3. Deploy the service.

## Security notes
- Keep `SESSION` and `OWNER_ID` secret.
- Admin commands require the user to be admin in groups; OWNER_ID is used for owner-only commands.
- Use `tags` and `broadcast` carefully to avoid spam and bans.
