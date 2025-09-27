from telethon import events
import asyncio

async def _is_admin(client, chat, user_id):
    try:
        p = await client.get_permissions(chat, user_id)
        return p.is_admin or p.is_creator
    except:
        return False

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!kick$", incoming=True))
    async def kick_handler(event):
        if not event.is_group:
            await event.reply("❌ This command can only be used in groups.")
            return
        if not await _is_admin(client, event.chat_id, event.sender_id):
            await event.reply("⚠️ You need to be an admin to use this command.")
            return
        if event.reply_to_msg_id:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
            try:
                await client.kick_participant(event.chat_id, user.id)
                await event.reply(f"👢 Kicked user: {user.id}")
            except Exception as e:
                await event.reply(f"❌ Kick failed: {e}")
        else:
            await event.reply("⚠️ Reply to a user's message to kick them.")

    @client.on(events.NewMessage(pattern=r"^!ban$", incoming=True))
    async def ban_handler(event):
        if not event.is_group:
            await event.reply("❌ This command can only be used in groups.")
            return
        if not await _is_admin(client, event.chat_id, event.sender_id):
            await event.reply("⚠️ You need to be an admin to use this command.")
            return
        if event.reply_to_msg_id:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
            try:
                await client.edit_permissions(event.chat_id, user.id, view_messages=False)
                await event.reply(f"⛔ Banned user: {user.id}")
            except Exception as e:
                await event.reply(f"❌ Ban failed: {e}")
        else:
            await event.reply("⚠️ Reply to a user's message to ban them.")

    @client.on(events.NewMessage(pattern=r"^!mute$", incoming=True))
    async def mute_handler(event):
        if not event.is_group:
            await event.reply("❌ This command can only be used in groups.")
            return
        if not await _is_admin(client, event.chat_id, event.sender_id):
            await event.reply("⚠️ You need to be an admin to use this command.")
            return
        if event.reply_to_msg_id:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
            try:
                await client.edit_permissions(event.chat_id, user.id, send_messages=False)
                await event.reply(f"🔇 Muted user: {user.id}")
            except Exception as e:
                await event.reply(f"❌ Mute failed: {e}")
        else:
            await event.reply("⚠️ Reply to a user's message to mute them.")

    @client.on(events.NewMessage(pattern=r"^!unmute$", incoming=True))
    async def unmute_handler(event):
        if not event.is_group:
            await event.reply("❌ This command can only be used in groups.")
            return
        if not await _is_admin(client, event.chat_id, event.sender_id):
            await event.reply("⚠️ You need to be an admin to use this command.")
            return
        if event.reply_to_msg_id:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
            try:
                await client.edit_permissions(event.chat_id, user.id, send_messages=True)
                await event.reply(f"🔊 Unmuted user: {user.id}")
            except Exception as e:
                await event.reply(f"❌ Unmute failed: {e}")
        else:
            await event.reply("⚠️ Reply to a user's message to unmute them.")

    @client.on(events.NewMessage(pattern=r"^!promote$", incoming=True))
    async def promote_handler(event):
        if not event.is_group:
            await event.reply("❌ This command can only be used in groups.")
            return
        if not await _is_admin(client, event.chat_id, event.sender_id):
            await event.reply("⚠️ You need to be an admin to use this command.")
            return
        if event.reply_to_msg_id:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
            try:
                await client.edit_admin(event.chat_id, user.id, is_admin=True, add_admins=True)
                await event.reply(f"✅ Promoted user: {user.id}")
            except Exception as e:
                await event.reply(f"❌ Promote failed: {e}")
        else:
            await event.reply("⚠️ Reply to a user's message to promote them.")

    @client.on(events.NewMessage(pattern=r"^!demote$", incoming=True))
    async def demote_handler(event):
        if not event.is_group:
            await event.reply("❌ This command can only be used in groups.")
            return
        if not await _is_admin(client, event.chat_id, event.sender_id):
            await event.reply("⚠️ You need to be an admin to use this command.")
            return
        if event.reply_to_msg_id:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
            try:
                await client.edit_admin(event.chat_id, user.id, is_admin=False)
                await event.reply(f"✅ Demoted user: {user.id}")
            except Exception as e:
                await event.reply(f"❌ Demote failed: {e}")
        else:
            await event.reply("⚠️ Reply to a user's message to demote them.")

    @client.on(events.NewMessage(pattern=r"^!purge\s*(\d+)?$", incoming=True))
    async def purge_handler(event):
        if not event.is_group:
            await event.reply("❌ This command can only be used in groups.")
            return
        if not await _is_admin(client, event.chat_id, event.sender_id):
            await event.reply("⚠️ You need to be an admin to use this command.")
            return
        count = 50
        if event.pattern_match.group(1):
            try:
                count = int(event.pattern_match.group(1))
            except:
                pass
        # delete last `count` messages from the chat (bot may only delete its own messages unless it's an admin)
        deleted = 0
        async for msg in client.iter_messages(event.chat_id, limit=count):
            try:
                await msg.delete()
                deleted += 1
            except:
                pass
        await event.reply(f"🧹 Purged ~{deleted} messages")
