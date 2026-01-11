import pathway as pw

def build_news_knowledge(news_table):
    return news_table.select(
        content=(
            "News update: " + news_table.title +
            ". Summary: " + news_table.summary +
            ". Sentiment: " + news_table.sentiment + "."
        ),
        timestamp=news_table.timestamp
    )

def build_stock_knowledge(stock_table):
    return stock_table.select(
        content=(
            "Stock update: " +
            stock_table.symbol +
            " price is " +
            pw.cast(str, stock_table.price) +
            " with volume " +
            pw.cast(str, stock_table.volume) +
            ". Signal: " +
            stock_table.price_signal
        ),
        timestamp=stock_table.timestamp
    )


def merge_knowledge(stock_knowledge, news_knowledge):
    return pw.concat(stock_knowledge, news_knowledge)