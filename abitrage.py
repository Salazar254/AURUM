# arbitrage.py

from exchange import binance, konwex, get_price, place_order
import config

def check_arbitrage():
    bnb_binance = get_price(binance, config.TRADING_PAIR)
    bnb_konwex = get_price(konwex, config.TRADING_PAIR)

    if not bnb_binance or not bnb_konwex:
        return None

    # Price differences
    diff1 = ((bnb_konwex - bnb_binance) / bnb_binance) * 100
    diff2 = ((bnb_binance - bnb_konwex) / bnb_konwex) * 100

    if diff1 > config.MIN_PROFIT_PERCENT:
        print(f"Buy Binance {bnb_binance}, Sell Konwex {bnb_konwex}, Profit: {diff1:.2f}%")
        # place_order(binance, "buy", config.TRADING_PAIR, config.TRADE_AMOUNT)
        # place_order(konwex, "sell", config.TRADING_PAIR, config.TRADE_AMOUNT)

    elif diff2 > config.MIN_PROFIT_PERCENT:
        print(f"Buy Konwex {bnb_konwex}, Sell Binance {bnb_binance}, Profit: {diff2:.2f}%")
        # place_order(konwex, "buy", config.TRADING_PAIR, config.TRADE_AMOUNT)
        # place_order(binance, "sell", config.TRADING_PAIR, config.TRADE_AMOUNT)
    else:
        print("No arbitrage opportunity.")
