# scanner.py

import time
import yfinance as yf
import pandas as pd
from strategy import generate_signal, calculate_multi_tp
from telegram import send_signal
from config import LOWER_TF, HIGHER_TF, SCAN_INTERVAL

# =========================
# SETTINGS
# =========================
NIFTY_SYMBOL = "^NSEI"

STOCKS = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "SBIN.NS"
]

LAST_SIGNAL = {}


# =========================
# DATA FETCH
# =========================
def fetch_data(symbol, interval, period="30d"):
    df = yf.download(
        symbol,
        interval=interval,
        period=period,
        progress=False
    )

    if df.empty or len(df) < 60:
        return None

    df = df.rename(columns=str.lower)
    return df


# =========================
# INDEX FILTER
# =========================
def index_trend_ok(nifty_df, side):
    close = nifty_df["close"].iloc[-1]
    ema50 = nifty_df["close"].ewm(span=50).mean().iloc[-1]

    if side == "BUY" and close > ema50:
        return True
    if side == "SELL" and close < ema50:
        return True

    return False


# =========================
# SCAN LOOP
# =========================
def scan_symbol(symbol):
    df_ltf = fetch_data(symbol, LOWER_TF)
    df_htf = fetch_data(symbol, HIGHER_TF)
    nifty_df = fetch_data(NIFTY_SYMBOL, HIGHER_TF)

    if df_ltf is None or df_htf is None or nifty_df is None:
        return

    signal = generate_signal(df_ltf, df_htf)
    if not signal:
        return

    if not index_trend_ok(nifty_df, signal["side"]):
        return

    key = (symbol, signal["side"])
    if LAST_SIGNAL.get(key):
        return

    LAST_SIGNAL[key] = True

    entry = df_ltf["close"].iloc[-1]
    levels = calculate_multi_tp(entry, signal["atr"], signal["side"])

    send_signal(
        symbol=symbol.replace(".NS", ""),
        tf=f"{LOWER_TF} → {HIGHER_TF}",
        side=signal["side"],
        entry=entry,
        sl=levels["sl"],
        tp1=levels["tp1"],
        tp2=levels["tp2"],
        tp3=levels["tp3"],
        confidence=signal["confidence"]
    )


def scanner_loop():
    while True:
        print("📊 NSE Scanner running...")
        for stock in STOCKS:
            scan_symbol(stock)

        time.sleep(SCAN_INTERVAL)
