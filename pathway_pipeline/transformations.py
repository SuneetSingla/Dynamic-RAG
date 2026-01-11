import pathway as pw

def add_features(stock_table):
    return stock_table.select(
        symbol = stock_table.symbol,
        price = stock_table.price,
        volume = stock_table.volume,
        timestamp = stock_table.timestamp,
        price_signal = pw.if_else(
            stock_table.price > 0,
            "price update received",
            "no data"
        )
    )
