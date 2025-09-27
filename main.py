import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Load secrets from environment
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

# Start the client
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(pattern="!ping"))
async def handler(event):
    await event.reply("pong ✅")

print("🚀 Userbot started...")
client.start()
client.run_until_disconnected()
