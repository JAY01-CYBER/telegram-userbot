from telethon import events

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!lock$", incoming=True))
    async def lock_handler(event):
        if not event.is_group:
            await event.reply("❌ Use in groups.")
            return
        me = await client.get_me()
        try:
            await client.edit_permissions(event.chat_id, me.id, send_messages=False)
            await event.reply("🔒 Chat locked.")
        except Exception as e:
            await event.reply(f"❌ Lock failed: {e}")

    @client.on(events.NewMessage(pattern=r"^!unlock$", incoming=True))
    async def unlock_handler(event):
        if not event.is_group:
            await event.reply("❌ Use in groups.")
            return
        me = await client.get_me()
        try:
            await client.edit_permissions(event.chat_id, me.id, send_messages=True)
            await event.reply("🔓 Chat unlocked.")
        except Exception as e:
            await event.reply(f"❌ Unlock failed: {e}")
