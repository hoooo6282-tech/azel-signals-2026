import os
import logging
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "").strip()

@app.get("/")
def health():
    return "Azel OTC Signals PRO is running", 200

@app.post("/webhook")
def webhook():
    if not WEBHOOK_SECRET or not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return jsonify({"ok": False, "error": "Server environment is not configured"}), 500

    data = request.get_json(silent=True) or {}
    if data.get("secret") != WEBHOOK_SECRET:
        return jsonify({"ok": False, "error": "Unauthorized"}), 401

    side = str(data.get("side", "")).upper()
    if side not in ("CALL", "PUT"):
        return jsonify({"ok": False, "error": "side must be CALL or PUT"}), 400

    symbol = str(data.get("symbol", "Unknown"))[:80]
    timeframe = str(data.get("timeframe", "1"))[:10]
    price = str(data.get("price", "—"))[:40]
    reason = str(data.get("reason", "Confirmed candle signal"))[:250]
    candle_time = str(data.get("time", "—"))[:50]

    emoji = "🟢" if side == "CALL" else "🔴"
    direction = "شراء CALL" if side == "CALL" else "بيع PUT"
    message = (
        "🔔 AZEL OTC SIGNALS PRO\\n"
        "━━━━━━━━━━━━━━\\n"
        f"{emoji} {direction}\\n"
        f"📊 الزوج: {symbol}\\n"
        f"⏱ الفريم: {timeframe} دقيقة\\n"
        f"💰 السعر وقت الإشارة: {price}\\n"
        f"🕒 وقت الشمعة: {candle_time}\\n"
        f"🧠 السبب: {reason}\\n"
        "━━━━━━━━━━━━━━\\n"
        "⚠️ إشارة تجريبية وليست ضماناً للربح. تحقق من تطابق السعر مع منصة التداول."
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            url,
            json={"chat_id": TELEGRAM_CHAT_ID, "text": message},
            timeout=15,
        )
        response.raise_for_status()
        result = response.json()
        if not result.get("ok"):
            return jsonify({"ok": False, "error": "Telegram rejected the message"}), 502
        return jsonify({"ok": True}), 200
    except requests.RequestException:
        logging.exception("Telegram send failed")
        return jsonify({"ok": False, "error": "Could not send Telegram message"}), 502

if __name__ == "__main__":
    port = int(os.getenv("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
