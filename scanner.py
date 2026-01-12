# scanner.py

import time
import requests
import pandas as pd
from strategy import generate_signal, calculate_multi_tp
from telegram import send_signal
from config import LOWER_TF, HIGHER_TF, SCAN_INTERVAL
import os

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

BASE_URL = "https://www.alphavantage.co/query"

# =========================
# SYMBOLS (BSE FORMAT)
# =========================
STOCKS = {
    "RELIANCE": "RELIANCE.BSE",
    "TCS": "TCS.BSE",
    "INFY": "INFY.BSE",
    "HDFCBANK": "HDFCBANK.BSE",
    "ICICIBANK": "ICICIBANK.BSE",
    "SBIN": "SBIN.BSE"
}

LAST_SIGNAL = {}

TF_MAP = {
    "15m": "15min",
    "1H": "60min",
    "1D": "DAILY"
}

# =========================
# FETCH DATA
# =========================
def fetch_candles(symbol, tf):
    function = (
        "TIME_SERIES_INTRADAY"
        if tf != "1D"
        else "TIME_SERIES_DAILY"
    )

    params = {
        "function": function,
        "symbol": symbol,
        "apikey": API_KEY,
        "outputsize": "compact"
    }

    if tf != "1D":
        params["interval"] = TF_MAP[tf]

    r = requests.get(BASE_URL, params=params, timeout=15)
    data = r.json()

    key = (
        f"Time Series ({TF_MAP[tf]})"
        if tf != "1D"
        else "Time Series (Daily)"
    )

    if key not in data:
        return None

    df = pd.DataFrame.from_dict(data[key], orient="index")
    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    })

    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    if len(df) < 60:
        return None

    return df

# =========================
# SCAN SYMBOL
# =========================
def scan_symbol(name, symbol):
    df_ltf = fetch_candles(symbol, LOWER_TF)
    time.sleep(12)  # rate limit safety

    df_htf = fetch_candles(symbol, HIGHER_TF)
    time.sleep(12)

    if df_ltf is None or df_htf is None:
        return

    signal = generate_signal(df_ltf, df_htf)
    if not signal:
        return

    key = (name, signal["side"])
    if LAST_SIGNAL.get(key):
        return

    LAST_SIGNAL[key] = True

    entry = df_ltf["close"].iloc[-1]
    levels = calculate_multi_tp(entry, signal["atr"], signal["side"])

    send_signal(
        symbol=name,
        tf=f"{LOWER_TF} → {HIGHER_TF}",
        side=signal["side"],
        entry=entry,
        sl=levels["sl"],
        tp1=levels["tp1"],
        tp2=levels["tp2"],
        tp3=levels["tp3"],
        confidence=signal["confidence"]
    )

# =========================
# MAIN LOOP
# =========================
def scanner_loop():
    while True:
        print("📡 Alpha Vantage NSE Scanner running...")
        for name, symbol in STOCKS.items():
            scan_symbol(name, symbol)

        time.sleep(SCAN_INTERVAL)
