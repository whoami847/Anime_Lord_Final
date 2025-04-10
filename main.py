import asyncio
from pyrogram import Client
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("anime_lord_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def start_bot():
    await app.start()
    print("Bot started. Running...")
    await idle()
    await app.stop()

if __name__ == "__main__":
    from pyrogram.idle import idle
    asyncio.run(start_bot())
