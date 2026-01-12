# main.py

import threading
import os
from flask import Flask, request
from scanner import scanner_loop
from zerodha_auth import generate_access_token

app = Flask(__name__)

@app.route("/")
def health():
    return "✅ Zerodha NSE Scanner Running", 200


# 🔑 Zerodha Redirect Handler
@app.route("/zerodha/callback")
def zerodha_callback():
    request_token = request.args.get("request_token")

    if not request_token:
        return "❌ Missing request_token", 400

    access_token = generate_access_token(request_token)

    return (
        "✅ Zerodha Login Successful<br>"
        "Access token generated.<br>"
        "Now update KITE_ACCESS_TOKEN in environment and restart."
    )


def start_scanner():
    print("🇮🇳 Zerodha Kite NSE Scanner Started")
    scanner_loop()


if __name__ == "__main__":
    threading.Thread(
        target=start_scanner,
        daemon=True
    ).start()

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
