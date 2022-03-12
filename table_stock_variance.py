#表出力
#stock data for excel
import pandas as pd
import yahoo_fin.stock_info as si
import plotly.graph_objects as go
from tickers import*
import os


ticker_main = []
ticker_name = []
for i in tickers5:
    ticker_main.append(i)
    ticker_name.append(i+'('+tickers5[i]+')')

header   = ['Ticker', 'Close','最大下落',
          '年初来*', '1ヶ月', '1週間', '1日']
title = "Watchlist"

df=pd.DataFrame()
for i in range(len(ticker_main)):
 data = si.get_data(ticker_main[i])
 #print(data)
 df.loc[ticker_main[i],'Ticker']=ticker_main[i]
 # +'('+ticker_name[i]+')'
 # print(df.loc[ticker_main[i],'Ticker'])

 stk_close=data["close"].iat[-1]
 df.loc[ticker_main[i],'Close']='%.2f'%(stk_close)

 # stk_adj=data["adjclose"].iat[-1]
 # df.loc[ticker_main[i],'Adj Close']='%.2f'%(stk_adj)

 # vol_today=data["volume"].iat[-1]
 # df.loc[ticker_main[i],'Volume(mil)']='{:,.0f}'.format(vol_today/100000)

 stk_max=data['close'].max()
 df.loc[ticker_main[i],'最大下落']='{:.2%}'.format((stk_close-stk_max)/stk_max)

 if '2020-12-31' in data.index:
     stk_yend=data.loc['2020-12-31','close']
     df.loc[ticker_main[i],'年初来*']='{:.2%}'.format((stk_close-stk_yend)/stk_yend)
 if '2020-12-31' not in data.index:
     stk_yend=data.loc[:,'close']
     df.loc[ticker_main[i],'年初来*']='{:.2%}'.format((stk_close-stk_yend[0])/stk_yend[0])
 if len(data)>=2:
     stk_yester=data['close'].iat[-2]
     df.loc[ticker_main[i],'1日']='{:.2%}'.format((stk_close-stk_yester)/stk_yester)
 if len(data)>=23:
     stk_month=data['close'].iat[-23]
     df.loc[ticker_main[i],'1ヶ月']='{:.2%}'.format((stk_close-stk_month)/stk_month)
 if len(data)>=5:
     stk_week=data['close'].iat[-5]
     df.loc[ticker_main[i],'1週間']='{:.2%}'.format((stk_close-stk_week)/stk_week)


 quot = si.get_quote_table(ticker_main[i], dict_result = True)
 # df.loc[ticker_main[i],'Market Cap']=""
 # df.loc[ticker_main[i],'PER']=0
#  if('Market Cap' in quot):
#    df.loc[ticker_main[i],'Market Cap']=quot['Market Cap']
#  if('PE Ratio (TTM)' in quot):
#    df.loc[ticker_main[i],'PER']=quot['PE Ratio (TTM)']
# #print(df)

fig = go.Figure(data=[go.Table(
  columnwidth = [100,50,50,50,50,50,50],
  header=dict(values=header, line_color='black', fill_color='white',
              align='center', font_size=16, height=30),
  cells=dict(values=[ticker_name , df['Close'], df['最大下落'], df['年初来*'], df['1ヶ月'],
             df['1週間'], df['1日']],
             line_color='black',
             fill_color=[['rgb(235, 235, 235)', 'white']*(int(len(ticker_main)/2)+1)],
             align=['center', 'right'],
             font_size=16, height=30)
  )],
)

title = title+ ' ('+data.index[-1].strftime('%Y/%m/%d')+')'

fig.update_layout(
  title={'text': title + '<br><sup>Takako(#FI): @snickersty</sup>', 'y': 0.9, 'x': 0.5},
  font={ 'family': 'Noto Sans CJK JP', 'size': 16},
  width=900
)
fig.add_annotation(dict(font=dict(color='blue',size=13),
                                        x=0,
                                        y=-0.05,
                                        showarrow=False,
                                        text="*: 去年末以降の上場は、上場初日から",
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

fig.show()

df.to_csv('stock.csv')
