import pathway as pw
from ingestion.news_ingest import news_stream
from ingestion.stock_ingest import stock_stream


def build_news_table():
    return pw.debug.table_from_rows(
        news_stream(),
        schema={
            "title": str,
            "summary": str,
            "sentiment": str,
            "timestamp": float
        }
    )


def build_stock_table():
    return pw.debug.table_from_rows(
        stock_stream(),
        schema={
            "symbol": str,
            "price": float,
            "volume": int,
            "timestamp": float
        }
    )
