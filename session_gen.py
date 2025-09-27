from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("=== Telegram Session String Generator ===")
api_id = int(input("Enter your API_ID: ").strip())
api_hash = input("Enter your API_HASH: ").strip()

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\n✅ Successfully logged in!")
    print("Your SESSION STRING (copy this to Render env variable):\n")
    print(client.session.save())
