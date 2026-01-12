# indicators.py

import pandas as pd

# =========================
# MOVING AVERAGE
# =========================
def moving_average(series, period):
    return series.rolling(period).mean()


# =========================
# TRUE RANGE
# =========================
def true_range(df):
    high_low = df["high"] - df["low"]
    high_close = (df["high"] - df["close"].shift()).abs()
    low_close = (df["low"] - df["close"].shift()).abs()

    return pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)


# =========================
# ATR
# =========================
def atr(df, period):
    tr = true_range(df)
    return tr.rolling(period).mean()


# =========================
# VOLUME SPIKE (FIXED)
# =========================
def volume_spike(volume, lookback, multiplier):
    avg_volume = volume.rolling(lookback).mean()

    if avg_volume.isna().all():
        return False

    latest_avg = avg_volume.iloc[-1]
    latest_vol = volume.iloc[-1]

    # 🔒 FORCE SCALARS
    latest_avg = float(latest_avg.item())
    latest_vol = float(latest_vol.item())

    if latest_avg <= 0:
        return False

    return latest_vol > latest_avg * multiplier


# =========================
# BREAKOUT DETECTION
# =========================
def breakout_high(df, lookback):
    recent_high = df["high"].rolling(lookback).max().iloc[-2]
    return float(df["close"].iloc[-1].item()) > float(recent_high.item())


def breakout_low(df, lookback):
    recent_low = df["low"].rolling(lookback).min().iloc[-2]
    return float(df["close"].iloc[-1].item()) < float(recent_low.item())
