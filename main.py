# main.py

import time
from arbitrage import check_arbitrage

if __name__ == "__main__":
    print("🚀 Starting Arbitrage Bot...")
    while True:
        check_arbitrage()
        time.sleep(5)  # check every 5 seconds
