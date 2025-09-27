from telethon import events
import wikipedia

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!wiki\s+(.+)", incoming=True))
    async def wiki_handler(event):
        query = event.pattern_match.group(1).strip()
        try:
            summary = wikipedia.summary(query, sentences=3)
            await event.reply(summary)
        except Exception as e:
            await event.reply(f"❌ Wiki error: {e}")
