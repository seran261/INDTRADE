# =========================
# MARKET / MODE
# =========================
MARKET = "INDIAN_EQUITY"
DATA_PROVIDER = "YFINANCE"

# =========================
# TIMEFRAMES
# =========================
# Entry timeframe
LOWER_TF = "15m"

# Trend / bias timeframe
HIGHER_TF = "1H"

# =========================
# SCAN CONTROL
# =========================
# Seconds between full scan loops
SCAN_INTERVAL = 300   # 5 minutes (safe for yfinance)

# =========================
# TREND SETTINGS
# =========================
MA_PERIOD = 50        # Moving average for trend

# =========================
# VOLUME FILTER
# =========================
VOLUME_LOOKBACK = 20
VOLUME_MULTIPLIER = 1.05   # relaxed for Indian equities

# =========================
# BREAKOUT FILTER
# =========================
BREAKOUT_LOOKBACK = 20

# =========================
# ATR / RISK MANAGEMENT
# =========================
ATR_PERIOD = 14

ATR_SL_MULTIPLIER = 1.0   # tighter SL for intraday

TP1_ATR = 0.8
TP2_ATR = 1.6
TP3_ATR = 2.5

# =========================
# CONFIDENCE SCORING
# =========================
WEIGHT_TREND_LTF = 25
WEIGHT_TREND_HTF = 30
WEIGHT_VOLUME    = 15
WEIGHT_BREAKOUT  = 20
WEIGHT_ATR       = 10

MIN_CONFIDENCE_SCORE = 20   # tuned to allow signals

# =========================
# SIGNAL CONTROL
# =========================
SIGNAL_COOLDOWN_ENABLED = True

# =========================
# MARKET SESSION (OPTIONAL)
# =========================
SESSION_START = "09:15"
SESSION_END   = "15:30"

USE_SESSION_FILTER = False  # enable later if needed
