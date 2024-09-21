import numpy as np
import pandas as pd
import pandas_datareader as web
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn

#select start date for correlation window as well as list of tickers
#start = datetime(2017, 1, 1)
symbols_list = ['CHPT', 'TSLA']