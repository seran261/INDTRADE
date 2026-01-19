# symbols.py
# NSE symbols for YFINANCE (.NS)

# =========================
# INDIAN INDICES (BIAS / HTF)
# =========================
INDICES = {
    "NIFTY50": "^NSEI",
    "BANKNIFTY": "^NSEBANK",
    "FINNIFTY": "^NIFTYFIN",
}

# =========================
# STOCK UNIVERSE (CUSTOM)
# =========================
STOCKS = {

    # =========================
    # ADANI GROUP
    # =========================
    "ADANIENT": "ADANIENT.NS",
    "ADANIPORTS": "ADANIPORTS.NS",
    "ADANIPOWER": "ADANIPOWER.NS",
    "ADANIGREEN": "ADANIGREEN.NS",
    "ADANITRANS": "ADANITRANS.NS",

    # =========================
    # CEMENT
    # =========================
    "AMBUJACEM": "AMBUJACEM.NS",
    "ACC": "ACC.NS",
    "DALBHARAT": "DALBHARAT.NS",
    "RAMCOCEM": "RAMCOCEM.NS",
    "SHREECEM": "SHREECEM.NS",
    "ULTRACEMCO": "ULTRACEMCO.NS",

    # =========================
    # BANKING & FINANCE
    # =========================
    "AXISBANK": "AXISBANK.NS",
    "BANDHANBNK": "BANDHANBNK.NS",
    "BANKBARODA": "BANKBARODA.NS",
    "CANBK": "CANBK.NS",
    "CHOLAFIN": "CHOLAFIN.NS",
    "FEDERALBNK": "FEDERALBNK.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "ICICIBANK": "ICICIBANK.NS",
    "IDFC": "IDFC.NS",
    "IDFCFIRSTB": "IDFCFIRSTB.NS",
    "INDUSINDBK": "INDUSINDBK.NS",
    "KOTAKBANK": "KOTAKBANK.NS",
    "LICHSGFIN": "LICHSGFIN.NS",
    "MANAPPURAM": "MANAPPURAM.NS",
    "MFSL": "MFSL.NS",
    "MUTHOOTFIN": "MUTHOOTFIN.NS",
    "PEL": "PEL.NS",
    "PNB": "PNB.NS",
    "RBLBANK": "RBLBANK.NS",
    "RECLTD": "RECLTD.NS",
    "SBICARD": "SBICARD.NS",
    "SBILIFE": "SBILIFE.NS",
    "SBIN": "SBIN.NS",
    "YESBANK": "YESBANK.NS",

    # =========================
    # IT & TECHNOLOGY
    # =========================
    "COFORGE": "COFORGE.NS",
    "HCLTECH": "HCLTECH.NS",
    "INFY": "INFY.NS",
    "LTIM": "LTIM.NS",
    "LTTS": "LTTS.NS",
    "MINDTREE": "MINDTREE.NS",
    "MPHASIS": "MPHASIS.NS",
    "OFSS": "OFSS.NS",
    "PERSISTENT": "PERSISTENT.NS",
    "TECHM": "TECHM.NS",
    "WIPRO": "WIPRO.NS",

    # =========================
    # FMCG & CONSUMER
    # =========================
    "ASIANPAINT": "ASIANPAINT.NS",
    "BERGEPAINT": "BERGEPAINT.NS",
    "BRITANNIA": "BRITANNIA.NS",
    "COLPAL": "COLPAL.NS",
    "DABUR": "DABUR.NS",
    "GODREJCP": "GODREJCP.NS",
    "HINDUNILVR": "HINDUNILVR.NS",
    "ITC": "ITC.NS",
    "MARICO": "MARICO.NS",
    "NESTLEIND": "NESTLEIND.NS",
    "PAGEIND": "PAGEIND.NS",
    "TATACONSUM": "TATACONSUM.NS",
    "TITAN": "TITAN.NS",
    "TRENT": "TRENT.NS",
    "UBL": "UBL.NS",

    # =========================
    # PHARMA & HEALTHCARE
    # =========================
    "APOLLOHOSP": "APOLLOHOSP.NS",
    "AUROPHARMA": "AUROPHARMA.NS",
    "BIOCON": "BIOCON.NS",
    "CIPLA": "CIPLA.NS",
    "DIVISLAB": "DIVISLAB.NS",
    "DRREDDY": "DRREDDY.NS",
    "GLAND": "GLAND.NS",
    "GLENMARK": "GLENMARK.NS",
    "LALPATHLAB": "LALPATHLAB.NS",
    "LUPIN": "LUPIN.NS",
    "METROPOLIS": "METROPOLIS.NS",
    "SUNPHARMA": "SUNPHARMA.NS",
    "SYNGENE": "SYNGENE.NS",
    "TORNTPHARM": "TORNTPHARM.NS",
    "ZYDUSLIFE": "ZYDUSLIFE.NS",

    # =========================
    # AUTO & ANCILLARY
    # =========================
    "APOLLOTYRE": "APOLLOTYRE.NS",
    "ASHOKLEY": "ASHOKLEY.NS",
    "BAJAJ-AUTO": "BAJAJ-AUTO.NS",
    "BALKRISIND": "BALKRISIND.NS",
    "BHARATFORG": "BHARATFORG.NS",
    "EICHERMOT": "EICHERMOT.NS",
    "ESCORTS": "ESCORTS.NS",
    "EXIDEIND": "EXIDEIND.NS",
    "HEROMOTOCO": "HEROMOTOCO.NS",
    "MARUTI": "MARUTI.NS",
    "MRF": "MRF.NS",
    "TATAMOTORS": "TATAMOTORS.NS",
    "TVSMOTOR": "TVSMOTOR.NS",

    # =========================
    # METALS / ENERGY / PSU
    # =========================
    "BHEL": "BHEL.NS",
    "COALINDIA": "COALINDIA.NS",
    "GAIL": "GAIL.NS",
    "HAL": "HAL.NS",
    "HINDALCO": "HINDALCO.NS",
    "HINDPETRO": "HINDPETRO.NS",
    "JSWENERGY": "JSWENERGY.NS",
    "JSWSTEEL": "JSWSTEEL.NS",
    "NMDC": "NMDC.NS",
    "NTPC": "NTPC.NS",
    "ONGC": "ONGC.NS",
    "PETRONET": "PETRONET.NS",
    "POWERGRID": "POWERGRID.NS",
    "SAIL": "SAIL.NS",
    "TATAPOWER": "TATAPOWER.NS",
    "TATASTEEL": "TATASTEEL.NS",
    "VEDL": "VEDL.NS",

    # =========================
    # REALTY / INFRA / OTHERS
    # =========================
    "DLF": "DLF.NS",
    "GMRINFRA": "GMRINFRA.NS",
    "GODREJPROP": "GODREJPROP.NS",
    "INDHOTEL": "INDHOTEL.NS",
    "IRCTC": "IRCTC.NS",
    "LT": "LT.NS",
    "MCX": "MCX.NS",
    "NAUKRI": "NAUKRI.NS",
    "OBEROIRLTY": "OBEROIRLTY.NS",
    "PVRINOX": "PVRINOX.NS",
    "SIEMENS": "SIEMENS.NS",
    "SUNTV": "SUNTV.NS",
    "TORNTPOWER": "TORNTPOWER.NS",
    "VOLTAS": "VOLTAS.NS",
    "WHIRLPOOL": "WHIRLPOOL.NS",
    "ZEEL": "ZEEL.NS",
}
