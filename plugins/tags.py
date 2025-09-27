from telethon import events
import asyncio

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!tags$", incoming=True))
    async def tags_all(event):
        if not event.is_group:
            await event.reply("⚠️ Use in groups only.")
            return
        async for user in client.iter_participants(event.chat_id):
            try:
                await event.reply(f"@{user.username}" if user.username else f"{user.id}")
                await asyncio.sleep(0.3)
            except:
                pass
