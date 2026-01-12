# =========================
# MARKET MODE
# =========================
MARKET = "INDIAN_EQUITY"
DATA_PROVIDER = "ALPHA_VANTAGE"

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
# (Keep >= 300 for Alpha Vantage free tier)
SCAN_INTERVAL = 300

# =========================
# TREND SETTINGS
# =========================
# Moving Average used for trend detection
MA_PERIOD = 50

# =========================
# VOLUME FILTER
# =========================
# Lookback candles for avg volume
VOLUME_LOOKBACK = 20

# Current volume must be X times avg volume
VOLUME_MULTIPLIER = 1.8

# =========================
# BREAKOUT FILTER
# =========================
# Lookback candles for high/low breakout
BREAKOUT_LOOKBACK = 20

# =========================
# ATR / RISK MANAGEMENT
# =========================
ATR_PERIOD = 14

# Stop loss = ATR * multiplier
ATR_SL_MULTIPLIER = 1.2

# Take-profit ladder (ATR multiples)
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

# Minimum score required to send signal
MIN_CONFIDENCE_SCORE = 55

# =========================
# SIGNAL CONTROL
# =========================
# Prevent duplicate signals per symbol per side
SIGNAL_COOLDOWN_ENABLED = True

# =========================
# MARKET SESSION (OPTIONAL)
# =========================
# Indian market hours (IST)
SESSION_START = "09:15"
SESSION_END   = "15:30"

USE_SESSION_FILTER = False  # turn ON later if needed
