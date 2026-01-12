def index_trend_ok(nifty_df, side):
    price = nifty_df["close"].iloc[-1]
    ema50 = nifty_df["close"].ewm(span=50).mean().iloc[-1]

    if side == "BUY" and price > ema50:
        return True
    if side == "SELL" and price < ema50:
        return True

    return False
