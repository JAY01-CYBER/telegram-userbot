from telethon import events

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!id$"))
    async def id_handler(event):
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user = await reply_msg.get_sender()
            await event.reply(f"📌 Replied user ID: `{user.id}`")
        else:
            user = await event.get_sender()
            await event.reply(f"📌 Your ID: `{user.id}`")
