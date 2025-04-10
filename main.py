from pyrogram import Client, filters
from flask import Flask, request
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Flask(__name__)
bot = Client("anime_lord", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

WEBHOOK_URL = "https://anime-lord.koyeb.app"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    bot.process_update(request.stream.read())
    return "OK"

@app.route("/", methods=["GET"])
def root():
    return "Bot Running (Webhook Mode)"

if __name__ == "__main__":
    import uvicorn

    # Telegram এর webhook সেট করা
    with bot:
        bot.set_webhook(url=f"{WEBHOOK_URL}/{BOT_TOKEN}")
    
    # Flask app চালানো
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
