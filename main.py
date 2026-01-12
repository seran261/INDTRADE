# main.py

import threading
import os
from flask import Flask
from scanner import scanner_loop

app = Flask(__name__)

@app.route("/")
def health():
    return "✅ Zerodha NSE Scanner Running", 200


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
