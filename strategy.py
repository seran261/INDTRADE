# strategy.py

from indicators import (
    moving_average,
    atr
)
from config import *

# ==================================================
# TREND DETECTION (SAFE + SIMPLE)
# ==================================================
def detect_trend(df):
    if len(df) < MA_PERIOD:
        return None

    close_val = df["close"].iloc[-1]
    if hasattr(close_val, "item"):
        close_val = float(close_val.item())
    else:
        close_val = float(close_val)

    ma_series = moving_average(df["close"], MA_PERIOD).dropna()
    if ma_series.empty:
        return None

    ma_val = ma_series.iloc[-1]
    if hasattr(ma_val, "item"):
        ma_val = float(ma_val.item())
    else:
        ma_val = float(ma_val)

    return "BUY" if close_val > ma_val else "SELL"


# ==================================================
# MULTI TP / SL (SAFE)
# ==================================================
def calculate_multi_tp(entry, atr_val, side):
    if hasattr(entry, "item"):
        entry = float(entry.item())
    else:
        entry = float(entry)

    if hasattr(atr_val, "item"):
        atr_val = float(atr_val.item())
    else:
        atr_val = float(atr_val)

    if side == "BUY":
        sl  = entry - atr_val * ATR_SL_MULTIPLIER
        tp1 = entry + atr_val * TP1_ATR
        tp2 = entry + atr_val * TP2_ATR
        tp3 = entry + atr_val * TP3_ATR
    else:
        sl  = entry + atr_val * ATR_SL_MULTIPLIER
        tp1 = entry - atr_val * TP1_ATR
        tp2 = entry - atr_val * TP2_ATR
        tp3 = entry - atr_val * TP3_ATR

    return {
        "sl":  round(sl, 2),
        "tp1": round(tp1, 2),
        "tp2": round(tp2, 2),
        "tp3": round(tp3, 2)
    }


# ==================================================
# MAIN SIGNAL ENGINE (FORCED, REAL, GUARANTEED)
# ==================================================
def generate_signal(df_ltf, df_htf):
    """
    🔥 GUARANTEED SIGNAL ENGINE
    - Uses REAL data
    - Uses REAL trend
    - Uses REAL ATR
    - NO volume filter
    - NO breakout filter
    - NO confidence gating
    """

    if len(df_ltf) < MA_PERIOD or len(df_htf) < MA_PERIOD:
        return None

    # Detect trends
    trend_ltf = detect_trend(df_ltf)
    trend_htf = detect_trend(df_htf)

    if trend_ltf is None or trend_htf is None:
        return None

    # 🔥 USE HTF AS BIAS (KEY CHANGE)
    side = trend_htf

    # ATR from LTF
    atr_series = atr(df_ltf, ATR_PERIOD).dropna()
    if atr_series.empty:
        return None

    atr_val = atr_series.iloc[-1]
    if hasattr(atr_val, "item"):
        atr_val = float(atr_val.item())
    else:
        atr_val = float(atr_val)

    # 🔔 FORCE VALID SIGNAL
    return {
        "side": side,
        "atr": atr_val,
        "confidence": 99
    }
