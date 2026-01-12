# symbols.py
# NSE symbols for YFINANCE intraday (.NS)

# =========================
# INDIAN INDICES (BIAS ONLY)
# =========================
INDICES = {
    "NIFTY50": "^NSEI",
    "BANKNIFTY": "^NSEBANK",
    "FINNIFTY": "^NIFTYFIN"
}

# =========================
# STOCK UNIVERSE
# =========================
STOCKS = {
    # CORE LARGE CAPS
    "RELIANCE": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "INFY": "INFY.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "ICICIBANK": "ICICIBANK.NS",
    "SBIN": "SBIN.NS",

    # BANKS
    "AXISBANK": "AXISBANK.NS",
    "KOTAKBANK": "KOTAKBANK.NS",
    "INDUSINDBK": "INDUSINDBK.NS",

    # IT
    "WIPRO": "WIPRO.NS",
    "HCLTECH": "HCLTECH.NS",
    "LTIM": "LTIM.NS",

    # FMCG
    "ITC": "ITC.NS",
    "HINDUNILVR": "HINDUNILVR.NS",

    # METALS / ENERGY
    "ONGC": "ONGC.NS",
    "TATASTEEL": "TATASTEEL.NS",
    "JSWSTEEL": "JSWSTEEL.NS",

    # INFRA
    "LT": "LT.NS",
    "ADANIPORTS": "ADANIPORTS.NS",

    # AUTO
    "TATAMOTORS": "TMCV.NS",
    "MARUTI": "MARUTI.NS",
}
