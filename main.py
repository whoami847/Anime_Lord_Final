from pyrogram import Client, filters, idle
import logging
from config import API_ID, API_HASH, BOT_TOKEN
from modules import all_features

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Client(
    "anime_lord_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register all handlers
all_features.register_handlers(bot)

if __name__ == "__main__":
    bot.start()
    print("Bot is up and running...")
    idle()
    bot.stop()
