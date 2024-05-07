# This package handle the data connection, parsing and notification

import yfinance as yahooFinance
import pandas as pd

from pytrade.domain.charts import Bar


class Yahoo:

    def last_day(self,sym):
        info = yahooFinance.Ticker(sym)
        pd.set_option('display.max_rows', None)
        df = info.history(period="1d")
        for index, row in df.iterrows():
            open = row['Open']
            high = row['High']
            low  = row["Low"]
            close = row["Close"]
            volume = row["Volume"]
            dividends = row["Dividends"]
            splits = row["Stock Splits"]
            bar = Bar(sym,high,low,open,close,volume,close)
            return bar


    def daily_prices(self,sym):
        info = yahooFinance.Ticker(sym)
        pd.set_option('display.max_rows', None)
        df = info.history(period="max")
        bars = []
        for index, row in df.iterrows():
            open = row['Open']
            high = row['High']
            low  = row["Low"]
            close = row["Close"]
            volume = row["Volume"]
            dividends = row["Dividends"]
            splits = row["Stock Splits"]
            bar = Bar(sym,high,low,open,close,volume,close)
            bars.append(bar)
        return bars




y = Yahoo()
bars = y.prices("META")
print(bars)