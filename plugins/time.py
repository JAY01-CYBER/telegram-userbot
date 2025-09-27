from telethon import events
from datetime import datetime
import pytz, os

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!time$", incoming=True))
    async def time_handler(event):
        tz = os.getenv('TIMEZONE', 'UTC')
        now = datetime.now(pytz.timezone(tz))
        await event.reply(f"🕒 Current time ({tz}): {now.strftime('%Y-%m-%d %H:%M:%S')}")
