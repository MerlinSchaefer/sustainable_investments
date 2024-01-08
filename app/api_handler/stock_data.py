from typing import Any

import yfinance as yf


def get_stock_data(ticker: str) -> Any:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist
