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


#Download data from Yahoo Finance using Yahoo Finance API, storing them in frames for better categorization
#Data preprocessing for all stock dataframes to make it easier to view/utilize for correlation calculations
frames = []
for stock in symbols:
    stock_curr = yf.download(stock, start=start_date, end=end_date)
    stock_curr.drop(columns = ['Open', 'High', 'Low', 'Close', 'Volume'], axis = 1, inplace = True)
    frames.append(stock_curr)

#Merge all stock frames along the first axis to prep data for correlation heat matrix
stocks_df = pd.concat(frames, axis = 1, keys = symbols)
print(stocks_df.head(5))
    
#Create a correlation matrix using panda's corr() method with the Pearson correlation method    
correlation_matrix = stocks_df.corr(method='pearson')
print(correlation_matrix.head(5))

print(sns.heatmap(stocks_df.corr(method='pearson')))


