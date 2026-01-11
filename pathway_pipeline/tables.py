import pathway as pw
from ingestion.news_ingest import news_stream
from ingestion.stock_ingest import stock_stream


def build_news_table():
    return pw.io.python.read(
        news_stream,
        schema={
            "title": str,
            "summary": str,
            "sentiment": str,
            "timestamp": float,
        },
        autocommit_duration_ms=1000,
    )


def build_stock_table():
    return pw.io.python.read(
        stock_stream,
        schema={
            "symbol": str,
            "price": float,
            "volume": int,
            "timestamp": float,
        },
        autocommit_duration_ms=1000,
    )
