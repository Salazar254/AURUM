# app.py
from flask import Flask, render_template, jsonify
from arbitrage import check_arbitrage
import threading, time

app = Flask(__name__)

# Shared data for frontend
latest_opportunity = {"message": "Bot not started yet."}

def run_bot():
    global latest_opportunity
    while True:
        result = check_arbitrage()
        if result:
            latest_opportunity = result
        time.sleep(5)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(latest_opportunity)

if __name__ == "__main__":
    # Run bot in background thread
    t = threading.Thread(target=run_bot, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=5000, debug=True)
