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
# VOLUME SPIKE
# =========================
def volume_spike(volume, lookback, multiplier):
    avg_volume = volume.rolling(lookback).mean()

    if avg_volume.iloc[-1] == 0:
        return False

    return volume.iloc[-1] > avg_volume.iloc[-1] * multiplier


# =========================
# BREAKOUT DETECTION
# =========================
def breakout_high(df, lookback):
    """
    Bullish breakout above recent high
    """
    recent_high = df["high"].rolling(lookback).max().iloc[-2]
    return df["close"].iloc[-1] > recent_high


def breakout_low(df, lookback):
    """
    Bearish breakdown below recent low
    """
    recent_low = df["low"].rolling(lookback).min().iloc[-2]
    return df["close"].iloc[-1] < recent_low
