import requests
from dotenv import load_dotenv

import os

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = f"https://azzeeezz.pythonanywhere.com/{BOT_TOKEN}"
requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}")
