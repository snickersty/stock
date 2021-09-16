#表出力
#stock data for excel
import pandas as pd
import yahoo_fin.stock_info as si
import plotly.graph_objects as go

tickers = ['AFRM', 'AAPL', 'AI', 'BABA', 'BIGC', 'BIIB', 'BMY', 'COST', 'CAT', 'COIN', 'COUR', 'CRWD', 'CVS', 'DDOG', 'DAL', 'DIS', 'DKNG', 'DOCS', 'DRVN', 'GDRX', 'EURN', 'GM', 'KOS', 'MAR', 'MAXR', 'MSFT', 'NKE', 'NFLX', 'OKTA', 'PFE', 'PG', 'PYPL', 'REGN', 'RBLX', 'SEER', 'SPCE', 'SBLK', 'TSLA', 'TSM', 'TTD', 'TWLO', 'U', 'V', 'VALE', 'VLDR', 'XMTR', 'ZM','GLD','HDV','SPYD','VYM','MGV','DIA','QQQ','VAW','VT','VTI','VWO','EWY','TUR','CADJPY=X','GBPJPY=X','EURJPY=X','SGDJPY=X','HKDJPY=X','JPY=X','CNYJPY=X']
#'VOO', 'TWTR', 'AMZN', 'OTLY', 'FB', 'TSLA', 'NVDA'
header   = ['Ticker', 'Close','Adj Close','Volume', 'Market Cap', 'PER','max drop',
          'YTD', '1mo', '1wk', '1d']
title = "Watchlist"

df=pd.DataFrame()
for i in range(len(tickers)):
 data = si.get_data(tickers[i])
 df.loc[tickers[i],'Ticker']=tickers[i]

 stk_close=data["close"].iat[-1]
 df.loc[tickers[i],'Close']='%.2f'%(stk_close)

 stk_adj=data["adjclose"].iat[-1]
 df.loc[tickers[i],'Adj Close']='%.2f'%(stk_adj)

 vol_today=data["volume"].iat[-1]
 df.loc[tickers[i],'Volume']=vol_today

 stk_max=data['close'].max()
 df.loc[tickers[i],'max drop']='{:.2%}'.format((stk_close-stk_max)/stk_max)

 if '2020-12-31' in data.index:
   stk_yend=data.loc['2020-12-31','close']
   df.loc[tickers[i],'YTD']='{:.2%}'.format((stk_close-stk_yend)/stk_yend)
 if len(data)>=2:
   stk_yester=data['close'].iat[-2]
   df.loc[tickers[i],'1d']='{:.2%}'.format((stk_close-stk_yester)/stk_yester)
 if len(data)>=23:
   stk_month=data['close'].iat[-23]
   df.loc[tickers[i],'1mo']='{:.2%}'.format((stk_close-stk_month)/stk_month)
 if len(data)>=5:
   stk_week=data['close'].iat[-5]
   df.loc[tickers[i],'1wk']='{:.2%}'.format((stk_close-stk_week)/stk_week)


 quot = si.get_quote_table(tickers[i], dict_result = True)
 # df.loc[tickers[i],'Market Cap']=""
 # df.loc[tickers[i],'PER']=0
 if('Market Cap' in quot):
   df.loc[tickers[i],'Market Cap']=quot['Market Cap']
 if('PE Ratio (TTM)' in quot):
   df.loc[tickers[i],'PER']=quot['PE Ratio (TTM)']
#print(df)

fig = go.Figure(data=[go.Table(
  header=dict(values=header, line_color='black', fill_color='white',
              align='center', font_size=16, height=30),
  cells=dict(values=[tickers, df['Adj Close'], df['Close'], df['Volume'], df['Market Cap'],
             df['PER'], df['max drop'], df['YTD'], df['1mo'],
             df['1wk'], df['1d']],
             line_color='black',
             fill_color=[['rgb(235, 235, 235)', 'white']*(int(len(tickers)/2)+1)],
             align=['center', 'right'],
             font_size=16, height=30)
  )],
)

title = title+ ' ('+data.index[-1].strftime('%Y/%m/%d')+')'
fig.update_layout(
  title={'text': title, 'y': 0.9, 'x': 0.5},
  font={ 'family': 'Noto Sans CJK JP', 'size': 16},
  width=1100
)
#fig.show()

df.to_csv('stock.csv')
