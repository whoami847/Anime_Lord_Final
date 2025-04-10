import os
from flask import Flask, request
from pyrogram import Client

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

WEBHOOK_URL = "https://anime-lord.koyeb.app"

app = Flask(__name__)
bot = Client("anime_lord", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    bot.process_update(request.stream.read())
    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "Bot is Running with Webhook"

if __name__ == "__main__":
    import uvicorn
    with bot:
        bot.set_webhook(url=f"{WEBHOOK_URL}/{BOT_TOKEN}")
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
