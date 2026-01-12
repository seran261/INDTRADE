# zerodha_auth.py

import os
from kiteconnect import KiteConnect

def generate_access_token(request_token):
    kite = KiteConnect(api_key=os.getenv("KITE_API_KEY"))

    data = kite.generate_session(
        request_token=request_token,
        api_secret=os.getenv("KITE_API_SECRET")
    )

    access_token = data["access_token"]
    print("✅ NEW ACCESS TOKEN:", access_token)

    return access_token
