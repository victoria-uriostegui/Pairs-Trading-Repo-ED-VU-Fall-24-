import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
from polygon import RESTClient
import yfinance as yf


#Set start date variable as start date for historical data (9/20/23)
start_date = dt.datetime(2023, 9, 20)
#Set end date variable as end date for historical data (9/20/24)
end_date = dt.datetime(2024, 9, 19)


#List of tickers for stocks to be compared (Auto Makers):
symbols = ['TSLA', 'BMWKY', 'FUJHY', 'DRPRY', 'HMC', 'KS', 'MZDAY', 'TM', 'HYMTF']

#List of tickers for stocks to be compared (EV Charging Companies):
symbols.extend(['CHPT', 'EVGO', 'BLNK', 'WBX', 'SPWRQ'])


#Dictionary variable to store the dataframes for each stock
stocks = {}

#Download data from Yahoo Finance using Yahoo Finance API, returns a data frame with stock data for that period 
for symbol in symbols:
    stocks[symbol] = yf.download(symbol, start=start_date, end=end_date)
    stocks[symbol]['Symbol'] = symbol


#Data preprocessing for all stock dataframes to make it easier to view/utilize for correlation calculations
for key in stocks:
    stocks[key].drop(columns = ['Symbol', 'Open', 'High', 'Low', 'Close', 'Volume'], axis = 0, inplace = True)
    stocks[key].drop('Date', axis=1, inplace=True)
    print("NA:", stocks[key].isna().sum())
    print(key, ":", stocks[key].head(3), '\n\n')
    stocks[key].reset_index(drop=True)
    

#stocks_df = pd.concat([])
#print(stocks_df)

#stocks_df = stocks_df.pivot(columns = 'Symbol', values = 'Close')
#print(stocks_df)

#correlation_df = stocks_df.corr(method='pearson')
#correlation_df.head().reset_index()
#del correlation_df.index.name
#print(correlation_df.head(10))


