#mplfinanceのインストール(必ずこのコードを最初に実行)
!pip install mplfinance

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import mplfinance as mpf

ticker = ('V')  #証券コード入力

#下記3行で日付入力
today_date = dt.date.today()
start = dt.datetime(2022,today_date.month,1) # datetime(年,月,日)
end = today_date

df = yf.download(ticker, start=start, end=end)  #株価取得(米株)
'''df.to_csv( "y_stock_data_"+ticker+".csv") #csvファイル取得

df.sort_values("Date",ascending=False) #株価取得'''

resampled=df.resample('W')  #週単位で集計

wdf = resampled.aggregate({'Open': 'first', 'High': 'max', 'Low': 'min',
                          'Close': 'last', 'Volume': 'sum'})  #集計結果

#下3行それぞれ10日、25日、200日移動平均線
df["ma10"] = df["Close"].rolling(window=10).mean()
df["ma25"] = df["Close"].rolling(window=25).mean()
df["ma200"] = df["Close"].rolling(window=200).mean()

cdf = df[start:end]
apd = [mpf.make_addplot(cdf["ma10"], color="blue"),
       mpf.make_addplot(cdf["ma25"], color="green"),
       mpf.make_addplot(cdf["ma200"], color="red"),]

mpf.plot(cdf, type='candle', figratio=(4,1), volume=True, addplot=apd)  #ローソク足チャート表示(下部分出来高)