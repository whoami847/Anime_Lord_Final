# File: config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Optional configs (if needed)
OWNER_ID = int(os.getenv("OWNER_ID", 0))  # আপনার ইউজার আইডি
DB_URL = os.getenv("DATABASE_URL", "")
