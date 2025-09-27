from telethon import events
import json, os

DB_FILE = 'notes_db.json'

def _load():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE,'r',encoding='utf-8') as f:
        return json.load(f)

def _save(d):
    with open(DB_FILE,'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False,indent=2)

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!note\s+add\s+(\S+)\s+(.+)", incoming=True))
    async def add_note(event):
        key = event.pattern_match.group(1)
        text = event.pattern_match.group(2)
        d = _load()
        d[key] = text
        _save(d)
        await event.reply(f"✅ Note saved: {key}")

    @client.on(events.NewMessage(pattern=r"^!note\s+get\s+(\S+)", incoming=True))
    async def get_note(event):
        key = event.pattern_match.group(1)
        d = _load()
        if key in d:
            await event.reply(f"🗒️ {key}: {d[key]}")
        else:
            await event.reply("❌ Note not found.")
