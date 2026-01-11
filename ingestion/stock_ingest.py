# ingestion/stock_ingest.py
import time
import requests
from config import SYMBOLS, POLL_INTERVAL, ALPHA_VANTAGE_KEY

def stock_stream():
    while True:
        for symbol in SYMBOLS:
            r = requests.get(
                f"https://www.alphavantage.co/query"
                f"?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_KEY}"
            ).json()

            data = r.get("Global Quote", {})
            if data:
                yield {
                    "symbol": symbol,
                    "price": float(data["05. price"]),
                    "volume": int(data["06. volume"]),
                    "timestamp": time.time()
                }

        time.sleep(POLL_INTERVAL)
