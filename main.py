import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Load secrets from environment
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

# Start the client
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

# --- Commands ---

# Ping command
@client.on(events.NewMessage(pattern="!ping"))
async def ping_handler(event):
    await event.reply("pong ✅")

# Alive command
@client.on(events.NewMessage(pattern="!alive"))
async def alive_handler(event):
    await event.reply("🤖 Userbot is alive and running on Render!")

# ID command (gets your Telegram ID or reply target's ID)
@client.on(events.NewMessage(pattern="!id"))
async def id_handler(event):
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        user = await reply_msg.get_sender()
        await event.reply(f"📌 Replied user ID: `{user.id}`")
    else:
        user = await event.get_sender()
        await event.reply(f"📌 Your ID: `{user.id}`")

# Help command
@client.on(events.NewMessage(pattern="!help"))
async def help_handler(event):
    commands = """
📖 **Userbot Commands**
- `!ping` → pong test
- `!alive` → check if bot is running
- `!id` → get your Telegram ID (or replied user’s ID)
- `!help` → show this help
"""
    await event.reply(commands)

# --- Start the bot ---
print("🚀 Userbot started...")
client.start()
client.run_until_disconnected()
