import requests
import time
from config import ALPHA_VANTAGE_KEY, POLL_INTERVAL

def fetch_news():
    url = (
        "https://www.alphavantage.co/query"
        f"?function=NEWS_SENTIMENT&apikey={ALPHA_VANTAGE_KEY}"
    )
    r = requests.get(url).json()
    news = r.get("feed", [])

    for item in news[:5]:
        yield {
            "title": item["title"],
            "summary": item["summary"],
            "sentiment": item["overall_sentiment_label"],
            "timestamp": time.time()
        }

def news_stream():
    while True:
        yield from fetch_news()
        time.sleep(POLL_INTERVAL)
