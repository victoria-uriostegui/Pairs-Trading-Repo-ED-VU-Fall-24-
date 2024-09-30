import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn
import yfinance as yf


#Set start date variable as start date for historical data (9/20/23)
start_date = dt.datetime(2023, 9, 20)
#Set end date variable as end date for historical data (9/20/24)
end_date = dt.datetime(2024, 9, 19)
#Array of tickers for selected stocks: CHPT (Charge Point) & TSLA (Tesla)
symbols_list = ['CHPT', 'TSLA']

#Download data from Yahoo Finance using Yahoo Finance API, returns a data frame with stock data for that period 
tsla_df = yf.download("TSLA", start=start_date, end=end_date)
tsla_df['Symbol'] = "TSLA"
#print(tsla_df)

chpt_df = yf.download("CHPT", start=start_date, end=end_date)
chpt_df['Symbol'] = "CHPT"
#print(chpt_df)

#Clean and transform the data to make it easier to view/utilize for correlation calculations
tsla = tsla_df[['Close', 'Symbol']]

#print(tsla)

chpt = chpt_df[[ 'Close', 'Symbol']]

stocks_df = pd.concat([tsla, chpt])
print(stocks_df)

stocks_df = stocks_df.pivot(columns = 'Symbol', values = 'Close')
print(stocks_df)

correlation_df = stocks_df.corr(method='pearson')
correlation_df.head().reset_index()
#del correlation_df.index.name
print(correlation_df.head(10))


