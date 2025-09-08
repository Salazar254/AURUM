# exchange.py

import ccxt
import config

# Initialize exchanges
binance = ccxt.binance({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY
})

konwex = ccxt.konwex({
    "apiKey": config.KONWEX_API_KEY,
    "secret": config.KONWEX_SECRET_KEY
})

def get_price(exchange, pair):
    """Get ticker price from exchange."""
    try:
        ticker = exchange.fetch_ticker(pair)
        return ticker["last"]
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def place_order(exchange, side, pair, amount):
    """Place a market order on exchange."""
    try:
        order = exchange.create_market_order(pair, side, amount)
        return order
    except Exception as e:
        print(f"Error placing order: {e}")
        return None
