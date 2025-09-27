from telethon import events
import random

JOKES = [
    "😂 Why don’t skeletons fight? They don’t have the guts.",
    "🤣 Parallel lines have so much in common… it’s a shame they’ll never meet.",
    "😅 Why was the math book sad? Because it had too many problems.",
]

QUOTES = [
    "🌟 Believe you can and you're halfway there.",
    "🔥 Push yourself, because no one else is going to do it for you.",
    "💡 Great things never come from comfort zones.",
]

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!joke$"))
    async def joke_handler(event):
        await event.reply(random.choice(JOKES))

    @client.on(events.NewMessage(pattern=r"^!quote$"))
    async def quote_handler(event):
        await event.reply(random.choice(QUOTES))
