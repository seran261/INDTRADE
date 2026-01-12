# scanner.py

import time
import yfinance as yf

from strategy import generate_signal, calculate_multi_tp
from telegram import send_signal
from config import LOWER_TF, HIGHER_TF, SCAN_INTERVAL
from symbols import STOCKS

# Prevent duplicate signals (per symbol + side)
LAST_SIGNAL = {}

# =========================
# FETCH CANDLES (YFINANCE)
# =========================
def fetch_candles(symbol, tf):
    interval_map = {
        "15m": "15m",
        "1H": "60m"
    }

    try:
        df = yf.download(
            symbol,
            interval=interval_map[tf],
            period="30d",
            progress=False,
            threads=False
        )

        if df is None or df.empty or len(df) < 60:
            return None

        df = df.rename(columns=str.lower)
        return df

    except Exception as e:
        print(f"⚠️ Data fetch error for {symbol} ({tf}) → {e}")
        return None


# =========================
# SCAN SINGLE SYMBOL
# =========================
def scan_symbol(name, symbol):
    df_ltf = fetch_candles(symbol, LOWER_TF)
    df_htf = fetch_candles(symbol, HIGHER_TF)

    if df_ltf is None or df_htf is None:
        return

    print(f"✅ Data OK for {name}")

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
# MAIN SCANNER LOOP
# =========================
def scanner_loop():
    print("📡 YFINANCE NSE Scanner running...")

    while True:
        for name, symbol in STOCKS.items():
            print(f"🔍 Scanning {name}")
            scan_symbol(name, symbol)

        time.sleep(SCAN_INTERVAL)
