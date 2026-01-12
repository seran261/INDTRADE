# main.py

import os
import threading
from flask import Flask, request
from kiteconnect import KiteConnect, exceptions
from scanner import scanner_loop
from zerodha_auth import generate_access_token

app = Flask(__name__)

def is_token_valid():
    try:
        kite = KiteConnect(api_key=os.getenv("KITE_API_KEY"))
        kite.set_access_token(os.getenv("KITE_ACCESS_TOKEN"))
        kite.profile()  # lightweight auth check
        return True
    except Exception as e:
        print("🔐 Zerodha token invalid:", e)
        return False


@app.route("/")
def health():
    return "Zerodha NSE Bot Running", 200


@app.route("/zerodha/callback")
def zerodha_callback():
    request_token = request.args.get("request_token")
    if not request_token:
        return "Missing request_token", 400

    access_token = generate_access_token(request_token)

    return (
        "Zerodha login successful.<br>"
        "Access token generated.<br>"
        "Update KITE_ACCESS_TOKEN env variable and restart."
    )


def start_scanner():
    if not is_token_valid():
        print("❌ Scanner NOT started — invalid Zerodha token")
        return

    print("✅ Zerodha token valid — starting scanner")
    scanner_loop()


if __name__ == "__main__":
    if is_token_valid():
        threading.Thread(target=start_scanner, daemon=True).start()
    else:
        print("⚠️ Waiting for Zerodha login")

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
