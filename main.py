# main.py

import threading
import os
from flask import Flask
from scanner import scanner_loop

# =========================
# FLASK APP
# =========================
app = Flask(__name__)


@app.route("/")
def health():
    return "✅ NSE Equity Scanner Running", 200


# =========================
# START SCANNER
# =========================
def start_scanner():
    print("🇮🇳 NSE SMART SCANNER STARTED")
    print("📊 Market : Indian Equity (NSE)")
    print("⏱ Timeframes configured")
    scanner_loop()


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    threading.Thread(
        target=start_scanner,
        daemon=True
    ).start()

    port = int(os.environ.get("PORT", 8080))
    app.run(
        host="0.0.0.0",
        port=port
    )
