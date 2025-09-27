from telethon import events
import requests

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!weather\s+(.+)", incoming=True))
    async def weather_handler(event):
        city = event.pattern_match.group(1).strip()
        try:
            r = requests.get(f"https://wttr.in/{city}?format=3", timeout=10)
            await event.reply(r.text)
        except Exception as e:
            await event.reply(f"❌ Weather error: {e}")
