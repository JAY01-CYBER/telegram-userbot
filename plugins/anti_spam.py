from telethon import events
import time, collections

# Very basic flood detector per user per chat
RATE_LIMIT = 5  # messages
WINDOW = 6      # seconds

user_times = {}  # {(chat_id, user_id): collections.deque([timestamps])}

def register(client, owner_id):
    @client.on(events.NewMessage(incoming=True))
    async def watch_msgs(event):
        if event.is_private:
            return
        key = (event.chat_id, event.sender_id)
        now = time.time()
        dq = user_times.get(key)
        if not dq:
            dq = collections.deque()
            user_times[key] = dq
        dq.append(now)
        # remove old
        while dq and dq[0] < now - WINDOW:
            dq.popleft()
        if len(dq) > RATE_LIMIT:
            try:
                await event.reply("⚠️ You are sending messages too fast. Please slow down.")
            except:
                pass
