#表出力
#stock data for excel
import pandas as pd
import yahoo_fin.stock_info as si
import plotly.graph_objects as go
from tickers import *
#tickers_list = ['AAPL','AFRM','CRWD', 'DDOG', 'DOCN', 'DOCS','ENPH', 'GOOGL','OKTA', 'DOCS', 'MTTR','NVDA','QCOM','RBLX','TTD','TSLA']

header   = ['Ticker', 'Close']
title = "Watchlist"


df=pd.DataFrame()
for i in range(len(tickers_list)):
  data = si.get_data(tickers_list[i])
  df.loc[tickers_list[i],'Ticker']=tickers_list[i]

  stk_close=data["close"].iat[-1]
  df.loc[tickers_list[i],'Close']='%.2f'%(stk_close)


fig = go.Figure(data=[go.Table(
  header=dict(values=header, line_color='black', fill_color='white',
              align='center', font_size=16, height=30),
  cells=dict(values=[df['Ticker'], df['Close']],
             line_color='black',
             fill_color=[['rgb(235, 235, 235)', 'white']*(int(len(tickers_list)/2)+1)],
             align=['center', 'right'],
             font_size=16, height=30)
  )],
)

title = title + ' ('+data.index[-1].strftime('%Y/%m/%d')+')'
fig.update_layout(
  title={'text': title, 'y': 1, 'x': 0.5},
  font={ 'family': 'Noto Sans CJK JP', 'size': 16},
  width=1100
)
#fig.show()

df.to_csv('stock_price.csv')
