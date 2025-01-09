# Download Apple stock data

import pandas as pd
import yfinance as yf

df = yf.download("AAPL",
start="2011-01-01",
end="2021-12-31",
progress=False)
# here progress=False is used to hide the progress bar

## Try using progress=True 

print(f"Downloaded {len(df)} rows of data.")
df.to_csv("AAPL.csv")
