from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    "anime_lord_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Import all handlers (auto-register via decorators)
import modules.all_features

if __name__ == "__main__":
    bot.start()
    print("Bot is running...")
    idle()
    bot.stop()
