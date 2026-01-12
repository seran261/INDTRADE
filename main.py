# main.py

import threading
import os
from flask import Flask
from scanner import scanner_loop

app = Flask(__name__)

@app.route("/")
def health():
    return "✅ NSE Scanner Running (Free Data Mode)", 200


def start_scanner():
    print("📊 NSE Scanner started (Alpha Vantage)")
    scanner_loop()


if __name__ == "__main__":
    threading.Thread(
        target=start_scanner,
        daemon=True
    ).start()

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
