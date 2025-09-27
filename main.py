import os
import glob
import importlib.util
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession

logging.basicConfig(level=logging.INFO)

# Load secrets from environment
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))  # Optional: your Telegram numeric ID

if not API_ID or not API_HASH or not SESSION:
    raise SystemExit("Please set API_ID, API_HASH and SESSION environment variables.")

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

def load_plugins():
    plugin_path = os.path.join(os.getcwd(), "plugins")
    if not os.path.isdir(plugin_path):
        print("No plugins folder found; creating one.")
        os.makedirs(plugin_path, exist_ok=True)
        return

    py_files = glob.glob(os.path.join(plugin_path, "*.py"))
    for file in py_files:
        module_name = os.path.basename(file)[:-3]
        try:
            spec = importlib.util.spec_from_file_location(module_name, file)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, "register"):
                mod.register(client, OWNER_ID)
            print(f"✅ Loaded plugin: {module_name}")
        except Exception as e:
            print(f"❌ Failed to load {module_name}: {e}")

load_plugins()

print("🚀 Userbot with plugins started...")
client.start()
client.run_until_disconnected()
