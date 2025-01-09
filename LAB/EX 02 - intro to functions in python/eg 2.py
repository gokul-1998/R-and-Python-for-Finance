# 1) Create a function to download stock data

import pandas as pd
import yfinance as yf

def download_stock_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    return df



# 2) using for loop, try to download data for 10 tickers using the function

import pandas as pd
import yfinance as yf

tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "FB", "TSLA", "NVDA", "NIO", "BABA", "BIDU"]

def download_stock_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    return df

for ticker in tickers:
    df = download_stock_data(ticker, "2011-01-01", "2021-12-31")
    df.to_csv(f"{ticker}.csv")