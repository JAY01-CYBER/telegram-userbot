import os
import glob
import importlib.util
from telethon import TelegramClient
from telethon.sessions import StringSession

# Load secrets from environment
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

# Start the client
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

# --- Plugin Loader ---
def load_plugins():
    plugin_path = os.path.join(os.getcwd(), "plugins")
    py_files = glob.glob(os.path.join(plugin_path, "*.py"))

    for file in py_files:
        module_name = os.path.basename(file)[:-3]
        spec = importlib.util.spec_from_file_location(module_name, file)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "register"):
            mod.register(client)
        print(f"✅ Loaded plugin: {module_name}")

# Load all plugins
load_plugins()

# --- Start the bot ---
print("🚀 Userbot with plugins started...")
client.start()
client.run_until_disconnected()
