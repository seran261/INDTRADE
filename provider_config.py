# provider_config.py

import os

# =========================
# ALPHA VANTAGE SETTINGS
# =========================
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

ALPHA_BASE_URL = "https://www.alphavantage.co/query"

# Rate-limit safety (seconds)
REQUEST_DELAY = 12

# Intraday output size
INTRADAY_OUTPUTSIZE = "compact"
