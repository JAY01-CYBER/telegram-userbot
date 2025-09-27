from telethon import events
import json, os

DB = 'broadcast_chats.json'

def _load():
    if not os.path.exists(DB):
        return []
    with open(DB,'r',encoding='utf-8') as f:
        return json.load(f)

def _save(lst):
    with open(DB,'w',encoding='utf-8') as f:
        json.dump(lst,f,ensure_ascii=False,indent=2)

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!broadcast\s+(.+)", incoming=True))
    async def broadcast_handler(event):
        if owner_id == 0 or event.sender_id != owner_id:
            await event.reply("⚠️ Owner-only command.")
            return
        text = event.pattern_match.group(1)
        chats = _load()
        sent = 0
        for c in chats:
            try:
                await client.send_message(c, text)
                sent += 1
            except:
                pass
        await event.reply(f"📣 Broadcast sent to {sent} chats.")

    @client.on(events.NewMessage(pattern=r"^!broadcast_add$", incoming=True))
    async def add_chat(event):
        if owner_id == 0 or event.sender_id != owner_id:
            await event.reply("⚠️ Owner-only command.")
            return
        chats = _load()
        if event.chat_id not in chats:
            chats.append(event.chat_id)
            _save(chats)
            await event.reply("✅ This chat was added to broadcast list.")
        else:
            await event.reply("❗ Already in list.")
