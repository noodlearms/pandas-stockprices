'''
Compare the value of $100 invested in two stocks over time
(ignoring dividends)

Apologies its still a bit rough as am a panda nube

Created on 17 Jun 2017

'''

# ----------------------------
stockcode1 = 'GOOG'
stockcode2 = 'AAPL'
# ----------------------------

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style 
from datetime import datetime 
import numpy as np
from pandas_datareader import data # installed the following using: conda install -c anaconda pandas-datareader=0.4.0

style.use('ggplot') # pre-defined matplotlib chart style (R style plot)

start = datetime(2010,1,1)
end = datetime(2017,6,17)

# get the price history of stock eg apple (AAPL) from the google API
# http://www.google.com/finance/historical?q=AAPL&startdate=Jan+01%2C+2000&output=csv
df = data.DataReader("AAPL", "google", start, end) 
df1 = data.DataReader("GOOG", "google", start, end)

df['daily_return'] = df['Close'].pct_change(1)
df['cum_return'] = df.daily_return.cumsum()
n,x = df.shape
df['val100']=np.nan
df.ix[0,'val100']=100
for i in range(1,n):
    df.ix[i,'val100']=df.ix[i-1,'val100']*(1+df.ix[i,'daily_return'])
print(df.head()) #print(df.tail())

df1['daily_return'] = df1['Close'].pct_change(1)
df1['cum_return'] = df1.daily_return.cumsum()
n,x = df1.shape
df1['val100']=np.nan
df1.ix[0,'val100']=100
for i in range(1,n):
    df1.ix[i,'val100']=df1.ix[i-1,'val100']*(1+df1.ix[i,'daily_return'])
print(df1.head()) #print(df1.tail())

''' this bit is not working yet
df_final = pd.DataFrame()
df_final['Date'] = df['Date'].copy()
df_final['AAPL'] = df['val100'].copy()
df_final['GOOG'] = df1.val100.copy()
df_final.head()
'''

# main plot
plotval100 = 1
if plotval100:
    ax = df.val100.plot(title='Value of $100 invested',legend=True)
    ax1 = df1.val100.plot(title='Value of $100 invested',legend=True)
    l = plt.legend()
    l.get_texts()[0].set_text('AAPL')
    l.get_texts()[1].set_text('GOOG')
    plt.show()


# some other random plots
plotprice = 0
if plotprice:
    ax = df['Close'].plot(title='Apple stock price') # add title to the pandas plot object
    ax.set_xlabel('time') # add xlabel to the matplotlib axes object
    ax.set_ylabel('price')
    #ax.title('Apple stock price')
    plt.show()

plotreturns = 0
if plotreturns:
    ax2 = df.daily_return.plot(title='Apple daily returns')
    plt.show()

plotcumreturns = 0
if plotcumreturns:
    ax2 = df.cum_return.plot(title='Apple cumulative daily returns')
    plt.show()
