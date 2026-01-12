# telegram.py

import requests
import os

# =========================
# TELEGRAM CONFIG
# =========================
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


# =========================
# UTILS
# =========================
def confidence_bar(score, length=10):
    filled = int((score / 100) * length)
    empty = length - filled
    return "▓" * filled + "░" * empty


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
# MAIN SIGNAL MESSAGE
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
        f"⚡ *Strategy* : 15m → 1H | Trend • Volume • Breakout • ATR\n"
        f"━━━━━━━━━━━━━━━━━━"
    )

    send(msg)


# =========================
# TEST SIGNAL (ONE-TIME)
# =========================
def send_test_signal():
    send_signal(
        symbol="TEST-STOCK",
        tf="15m → 1H",
        side="BUY",
        entry=100.50,
        sl=98.90,
        tp1=102.00,
        tp2=104.00,
        tp3=107.00,
        confidence=99
    )
