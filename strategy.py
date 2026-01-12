# strategy.py

from indicators import (
    moving_average,
    volume_spike,
    breakout_high,
    breakout_low,
    atr
)
from config import *

# =========================
# TREND DETECTION (SAFE)
# =========================
def detect_trend(df):
    if len(df) < MA_PERIOD:
        return None

    close_price = float(df["close"].iloc[-1].item())
    ma_series = moving_average(df["close"], MA_PERIOD)

    if ma_series.isna().all():
        return None

    ma_value = float(ma_series.iloc[-1].item())

    return "BUY" if close_price > ma_value else "SELL"


# =========================
# MULTI TP / SL
# =========================
def calculate_multi_tp(entry, atr_val, side):
    entry = float(entry)
    atr_val = float(atr_val)

    if side == "BUY":
        tp1 = entry + atr_val * TP1_ATR
        tp2 = entry + atr_val * TP2_ATR
        tp3 = entry + atr_val * TP3_ATR
        sl  = entry - atr_val * ATR_SL_MULTIPLIER
    else:
        tp1 = entry - atr_val * TP1_ATR
        tp2 = entry - atr_val * TP2_ATR
        tp3 = entry - atr_val * TP3_ATR
        sl  = entry + atr_val * ATR_SL_MULTIPLIER

    return {
        "tp1": round(tp1, 2),
        "tp2": round(tp2, 2),
        "tp3": round(tp3, 2),
        "sl":  round(sl, 2)
    }


# =========================
# CONFIDENCE SCORE
# =========================
def confidence_score(trend_ltf, trend_htf, vol_ok, breakout_ok, atr_ok):
    score = 0

    if trend_ltf:
        score += WEIGHT_TREND_LTF

    if trend_htf and trend_ltf == trend_htf:
        score += WEIGHT_TREND_HTF

    if vol_ok:
        score += WEIGHT_VOLUME

    if breakout_ok:
        score += WEIGHT_BREAKOUT

    if atr_ok:
        score += WEIGHT_ATR

    return score


# =========================
# MAIN SIGNAL ENGINE
# =========================
def generate_signal(df_ltf, df_htf):
    min_len = max(
        MA_PERIOD,
        ATR_PERIOD,
        BREAKOUT_LOOKBACK,
        VOLUME_LOOKBACK
    )

    if len(df_ltf) < min_len or len(df_htf) < min_len:
        return None

    trend_ltf = detect_trend(df_ltf)
    trend_htf = detect_trend(df_htf)

    if trend_ltf is None or trend_htf is None:
        return None

    # Require alignment
    if trend_ltf != trend_htf:
        return None

    # Volume
    vol_ok = volume_spike(
        df_ltf["volume"],
        VOLUME_LOOKBACK,
        VOLUME_MULTIPLIER
    )

    # Breakout
    breakout_ok = (
        breakout_high(df_ltf, BREAKOUT_LOOKBACK)
        if trend_ltf == "BUY"
        else breakout_low(df_ltf, BREAKOUT_LOOKBACK)
    )

    if not (vol_ok or breakout_ok):
        return None

    atr_series = atr(df_ltf, ATR_PERIOD)
    if atr_series.isna().all():
        return None

    atr_val = float(atr_series.iloc[-1].item())
    atr_mean = float(atr_series.mean().item())

    atr_ok = atr_val > atr_mean

    score = confidence_score(
        trend_ltf,
        trend_htf,
        vol_ok,
        breakout_ok,
        atr_ok
    )

    if score < MIN_CONFIDENCE_SCORE:
        return None

    return {
        "side": trend_ltf,
        "atr": atr_val,
        "confidence": score
    }
