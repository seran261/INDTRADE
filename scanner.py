# scanner.py

import time
import pandas as pd
from kiteconnect import KiteConnect
from strategy import generate_signal, calculate_multi_tp
from telegram import send_signal
from config import LOWER_TF, HIGHER_TF, SCAN_INTERVAL
import os

# =========================
# ZERODHA AUTH
# =========================
kite = KiteConnect(api_key=os.getenv("KITE_API_KEY"))
kite.set_access_token(os.getenv("KITE_ACCESS_TOKEN"))

# =========================
# SYMBOL CONFIG
# =========================
NIFTY_TOKEN = 256265  # NIFTY 50 instrument token

STOCKS = {
    "RELIANCE": 738561,
    "TCS": 2953217,
    "INFY": 408065,
    "HDFCBANK": 341249,
    "ICICIBANK": 1270529,
    "SBIN": 779521
}

LAST_SIGNAL = {}

# =========================
# TIMEFRAME MAP
# =========================
TF_MAP = {
    "15m": "15minute",
    "1H": "60minute",
    "1D": "day"
}

# =========================
# DATA FETCH
# =========================
def fetch_candles(token, tf, days=30):
    data = kite.historical_data(
        instrument_token=token,
        from_date=pd.Timestamp.now() - pd.Timedelta(days=days),
        to_date=pd.Timestamp.now(),
        interval=TF_MAP[tf]
    )

    if not data or len(data) < 60:
        return None

    df = pd.DataFrame(data)
    df.set_index("date", inplace=True)
    return df


# =========================
# NIFTY FILTER
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
# SCANNER LOOP
# =========================
def scan_symbol(name, token):
    df_ltf = fetch_candles(token, LOWER_TF)
    df_htf = fetch_candles(token, HIGHER_TF)
    nifty_df = fetch_candles(NIFTY_TOKEN, HIGHER_TF)

    if df_ltf is None or df_htf is None or nifty_df is None:
        return

    signal = generate_signal(df_ltf, df_htf)
    if not signal:
        return

    if not index_trend_ok(nifty_df, signal["side"]):
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


def scanner_loop():
    while True:
        print("📡 Zerodha NSE Scanner running...")
        for name, token in STOCKS.items():
            scan_symbol(name, token)

        time.sleep(SCAN_INTERVAL)
