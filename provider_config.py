# provider_config.py

# =========================
# YFINANCE SETTINGS
# =========================

# Number of days of history to fetch
HISTORY_DAYS = 30

# Minimum candles required to process
MIN_CANDLES_REQUIRED = 60

# Retry logic
FETCH_RETRIES = 3
RETRY_DELAY_SECONDS = 3

# Disable threading for stability
YF_THREADS = False
