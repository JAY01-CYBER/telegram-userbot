from telethon import events
import os

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!alive$"))
    async def alive_handler(event):
        await event.reply(f"🤖 Userbot is alive! Running as: @{(await client.get_me()).username if (await client.get_me()).username else 'me'}")
