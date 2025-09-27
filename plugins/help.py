from telethon import events

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!help$"))
    async def help_handler(event):
        commands = """
📖 **Userbot Commands (stable)**
- `!ping` → pong test
- `!alive` → check if bot is running
- `!id` → get your Telegram ID (or replied user’s ID)
- `!help` → show this help
- `!joke` / `!quote` → fun
- `!wiki <term>` → wikipedia lookup
- `!weather <city>` → simple weather (wttr.in)
- `!calc <expression>` → calculator
- `!time` → show current time
- `!note add <key> <text>` → save a note
- `!note get <key>` → retrieve a note
- `!tags` → mention all members (use with care)
- `!kick` / `!ban` / `!mute` / `!unmute` / `!promote` / `!demote` / `!purge` → admin tools
- `!broadcast <text>` → owner-only broadcast
- `!remind <seconds> <text>` → set a reminder
- `!lock` / `!unlock` → admin lock chat
"""
        await event.reply(commands)
