from telethon import events

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!ping$"))
    async def ping_handler(event):
        await event.reply("pong ✅")
