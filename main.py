import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

# Dummy web server for Koyeb
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_web_server():
    server = HTTPServer(("0.0.0.0", 8080), HealthCheckHandler)
    server.serve_forever()

# Define the bot client
bot = Client(
    "anime_lord_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Import all command handlers
import modules.all_features

if __name__ == "__main__":
    threading.Thread(target=run_web_server).start()  # Start web server in background
    bot.start()
    print("Bot is running...")
    idle()
    bot.stop()
