# telegram_config.py

import os

# =========================
# TELEGRAM TOGGLE
# =========================
TELEGRAM_ENABLED = True

# =========================
# TELEGRAM CREDS
# =========================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# =========================
# MESSAGE STYLE
# =========================
SHOW_CONFIDENCE_BAR = True
SHOW_TP_LADDER = True

# Emojis
BUY_EMOJI = "🟢🚀"
SELL_EMOJI = "🔴📉"
