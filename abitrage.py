# arbitrage.py
from exchange import binance, konwex, get_price
import config

def check_arbitrage():
    bnb_binance = get_price(binance, config.TRADING_PAIR)
    bnb_konwex = get_price(konwex, config.TRADING_PAIR)

    if not bnb_binance or not bnb_konwex:
        return {"message": "Error fetching prices."}

    # Price differences
    diff1 = ((bnb_konwex - bnb_binance) / bnb_binance) * 100
    diff2 = ((bnb_binance - bnb_konwex) / bnb_konwex) * 100

    if diff1 > config.MIN_PROFIT_PERCENT:
        return {
            "message": f"Buy Binance {bnb_binance}, Sell Konwex {bnb_konwex}, Profit: {diff1:.2f}%",
            "buy": "Binance",
            "sell": "Konwex",
            "profit": round(diff1, 2)
        }

    elif diff2 > config.MIN_PROFIT_PERCENT:
        return {
            "message": f"Buy Konwex {bnb_konwex}, Sell Binance {bnb_binance}, Profit: {diff2:.2f}%",
            "buy": "Konwex",
            "sell": "Binance",
            "profit": round(diff2, 2)
        }

    return {"message": "No arbitrage opportunity."}
