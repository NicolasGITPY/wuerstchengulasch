import datetime as dt
from mpl_finance import candlestick_ohlc
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mpl_finance 

# define timeframe

start = dt.datetime(2020, 1, 20)
end = dt.datetime.now()

# load data

data = web.DataReader('TSLA', 'yahoo', start, end)

# restructure data 

data = data[['Open','High','Low', 'Close']]

data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)
print(data.head())

# Visualization

ax = plt.subplot()
ax.grid(True)
ax.set_title('TSLA share price', color = 'white')
ax.set_axisbelow(True)
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width = 0.5, colorup = '#00ff00')
plt.show()