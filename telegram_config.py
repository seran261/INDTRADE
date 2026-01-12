# telegram_config.py

import os

TELEGRAM_ENABLED = True

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Emojis / style
SHOW_CONFIDENCE_BAR = True
SHOW_TP_LADDER = True
