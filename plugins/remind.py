from telethon import events
import threading, time, json, os

DB = 'reminders.json'

def _load():
    if not os.path.exists(DB):
        return []
    with open(DB,'r',encoding='utf-8') as f:
        return json.load(f)

def _save(lst):
    with open(DB,'w',encoding='utf-8') as f:
        json.dump(lst,f,ensure_ascii=False,indent=2)

def _run_reminder(client, chat_id, text, remind_at):
    now = time.time()
    delay = max(0, remind_at - now)
    def _job():
        time.sleep(delay)
        try:
            client.loop.create_task(client.send_message(chat_id, f"⏰ Reminder: {text}"))
        except:
            pass
    t = threading.Thread(target=_job)
    t.daemon = True
    t.start()

def register(client, owner_id):
    # load persisted reminders
    for r in _load():
        _run_reminder(client, r['chat_id'], r['text'], r['at'])
    @client.on(events.NewMessage(pattern=r"^!remind\s+(\d+)\s+(.+)", incoming=True))
    async def remind_handler(event):
        seconds = int(event.pattern_match.group(1))
        text = event.pattern_match.group(2)
        at = time.time() + seconds
        lst = _load()
        lst.append({'chat_id': event.chat_id, 'text': text, 'at': at})
        _save(lst)
        _run_reminder(client, event.chat_id, text, at)
        await event.reply(f"✅ Reminder set for {seconds} seconds from now.")
