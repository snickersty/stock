#表出力
#stock data for excel
import pandas as pd
import yahoo_fin.stock_info as si
import plotly.graph_objects as go
from tickers import*

header   = ['Ticker', 'Close','Adj Close','Max','Min','Volume', 
          'max drop','YTD', '1mo', '1wk', '1d'] #'Market Cap',
title = "Watchlist"
#print(si.get_data('AAPL'))

df=pd.DataFrame()
for i in range(len(tickers_list)):
  data = si.get_data(tickers_list[i])
  df.loc[tickers_list[i],'Ticker']=tickers_list[i]
  #print(data,tickers_list[i])

  stk_close=data["close"].iat[-1]
  df.loc[tickers_list[i],'Close']='%.2f'%(stk_close)

  stk_adj=data["adjclose"].iat[-1]
  df.loc[tickers_list[i],'Adj Close']='%.2f'%(stk_adj)

  vol_today=data["volume"].iat[-1]
  df.loc[tickers_list[i],'Volume']=vol_today

  stk_max=data['close'].max()
  stk_min=data['close'][-180:].min()
  df.loc[tickers_list[i],'Max']='%.2f'%(stk_max)
  df.loc[tickers_list[i],'min']='%.2f'%(stk_min)
  df.loc[tickers_list[i],'max drop']='{:.2%}'.format((stk_close-stk_max)/stk_max)

  if '2021-12-31' in data.index:
    stk_yend=data.loc['2021-12-31','close']
    df.loc[tickers_list[i],'YTD']='{:.2%}'.format((stk_close-stk_yend)/stk_yend)
  if '2021-12-31' not in data.index:
      stk_yend=data.loc[:,'close']
      df.loc[tickers_list[i],'YTD']='{:.2%}'.format((stk_close-stk_yend[0])/stk_yend[0])
  if len(data)>=2:
    stk_yester=data['close'].iat[-2]
    df.loc[tickers_list[i],'1d']='{:.2%}'.format((stk_close-stk_yester)/stk_yester)
  if len(data)>=22:
    stk_month=data['close'].iat[-22]
    df.loc[tickers_list[i],'1mo']='{:.2%}'.format((stk_close-stk_month)/stk_month)
  if len(data)>=5:
    stk_week=data['close'].iat[-5]
    df.loc[tickers_list[i],'1wk']='{:.2%}'.format((stk_close-stk_week)/stk_week)

'''
  quot = si.get_quote_table(tickers_list[i], dict_result = True)
  # df.loc[tickers_list[i],'Market Cap']=""
  # df.loc[tickers_list[i],'PER']=0
  if('Market Cap' in quot):
    df.loc[tickers_list[i],'Market Cap']=quot['Market Cap']
  # if('PE Ratio (TTM)' in quot):
  #   df.loc[tickers_list[i],'PER']=quot['PE Ratio (TTM)']

  df['new'] = df['YTD'].str.strip('%').astype(float)
  '''
sorted_df = df.sort_values(by=['Ticker'], ascending=True)
  #print(sorted_df)


fig = go.Figure(data=[go.Table(
  header=dict(values=header, line_color='black', fill_color='white',
              align='center', font_size=16, height=30),
  cells=dict(values=[sorted_df['Ticker'], sorted_df['Close'], sorted_df['Adj Close'], 
             sorted_df['Max'],sorted_df['min'], sorted_df['Volume'], #sorted_df['Market Cap'],
             sorted_df['max drop'], sorted_df['YTD'], sorted_df['1mo'],
             sorted_df['1wk'], sorted_df['1d']],
             line_color='black',
             fill_color=[['rgb(235, 235, 235)', 'white']*(int(len(tickers_list)/2)+1)],
             align=['center', 'right'],
             font_size=16, height=30)
  )],
)
'''
title = title + ' ('+data.index[-1].strftime('%Y/%m/%d')+')'
fig.update_layout(
  title={'text': title, 'y': 1, 'x': 0.5},
  font={ 'family': 'Noto Sans CJK JP', 'size': 16},
  width=1100
)
fig.show()
'''
sorted_df.to_csv('stock_price.csv')
