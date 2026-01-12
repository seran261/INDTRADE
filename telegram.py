# telegram.py

import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


# =========================
# UTILS
# =========================
def confidence_bar(score, length=10):
    filled = int((score / 100) * length)
    return "▓" * filled + "░" * (length - filled)


def market_bias(side):
    return "📈 Bullish" if side == "BUY" else "📉 Bearish"


def send(msg):
    requests.post(
        API_URL,
        json={
            "chat_id": CHAT_ID,
            "text": msg,
            "parse_mode": "Markdown"
        },
        timeout=10
    )


# =========================
# SIGNAL MESSAGE
# =========================
def send_signal(symbol, tf, side, entry, sl, tp1, tp2, tp3, confidence):
    emoji = "🟢🚀" if side == "BUY" else "🔴📉"
    fire = "🔥🔥" if confidence >= 80 else "🔥"

    msg = (
        f"{emoji} *NSE SMART TRADE SIGNAL*\n"
        f"━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 *Stock* : `{symbol}`\n"
        f"⏱ *TF*    : `{tf}`\n"
        f"🧠 *Bias* : *{market_bias(side)}*\n\n"
        f"💰 *ENTRY* : `{round(entry,2)}`\n"
        f"🛑 *SL*    : `{sl}`\n\n"
        f"🎯 *TARGETS*\n"
        f"➤ TP1 : `{tp1}`\n"
        f"➤ TP2 : `{tp2}`\n"
        f"➤ TP3 : `{tp3}`\n\n"
        f"{fire} *CONFIDENCE*\n"
        f"`{confidence}/100`\n"
        f"`{confidence_bar(confidence)}`\n\n"
        f"📊 *Index Aligned (NIFTY)*\n"
        f"⚡ *Strategy* : Trend • Volume • Breakout • ATR\n\n"
        f"━━━━━━━━━━━━━━━━━━"
    )

    send(msg)
