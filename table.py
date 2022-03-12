#表出力
import sys
sys.path.append('/content/drive/MyDrive/module')
import pandas as pd
import yahoo_fin.stock_info as si
import plotly.graph_objects as go

tickers = ['AFRM', 'AAPL', 'AI', 'BABA', 'BIGC', 'BIIB', 'BMY', 'COST', 'CAT', 'COIN', 'COUR', 'CRWD', 'CVS', 'DDOG', 'DAL', 'DIS', 'DKNG', 'DOCS', 'DRVN', 'GDRX', 'EURN', 'GM', 'KOS', 'MAR', 'MAXR', 'MSFT', 'NKE', 'NFLX', 'OKTA', 'PFE', 'PG', 'PYPL', 'REGN', 'RBLX', 'SEER', 'SPCE', 'SBLK', 'TSLA', 'TSM', 'TTD', 'TWLO', 'U', 'V', 'VALE', 'VLDR', 'XMTR', 'ZM']
#'VOO', 'TWTR', 'AMZN', 'OTLY', 'FB', 'TSLA', 'NVDA'
header   = ['Ticker','現在値', '出来高', '時価総額', 'PER','高値下落',
          '年初来', '１ヶ月', '１週間', '１日']

title = "ウォッチリストデータ"

df=pd.DataFrame()
for i in range(len(tickers)):
 data = si.get_data(tickers[i])
 df.loc[tickers[i],'Ticker']=tickers[i]

 stk_today=data["adjclose"].iat[-1]
 df.loc[tickers[i],'現在値']='$%.2f'%(stk_today)

 vol_today=data["volume"].iat[-1]
 df.loc[tickers[i],'出来高']=vol_today
 stk_max=data['adjclose'].max()
 df.loc[tickers[i],'高値下落']='{:.2%}'.format((stk_today-stk_max)/stk_max)

 if '2020-12-31' in data.index:
   stk_yend=data.loc['2020-12-31','adjclose']
   df.loc[tickers[i],'年初来']='{:.2%}'.format((stk_today-stk_yend)/stk_yend)
 if len(data)>=2:
   stk_yester=data['adjclose'].iat[-2]
   df.loc[tickers[i],'１日']='{:.2%}'.format((stk_today-stk_yester)/stk_yester)
 if len(data)>=23:
   stk_month=data['adjclose'].iat[-23]
   df.loc[tickers[i],'１ヶ月']='{:.2%}'.format((stk_today-stk_month)/stk_month)
 if len(data)>=5:
   stk_week=data['adjclose'].iat[-5]
   df.loc[tickers[i],'１週間']='{:.2%}'.format((stk_today-stk_week)/stk_week)

 quot = si.get_quote_table(tickers[i], dict_result = True)
 df.loc[tickers[i],'時価総額']=""
 df.loc[tickers[i],'PER']=0
 if('Market Cap' in quot):
   df.loc[tickers[i],'時価総額']=quot['Market Cap']
 if('PE Ratio (TTM)' in quot):
   df.loc[tickers[i],'PER']=quot['PE Ratio (TTM)']

fig = go.Figure(data=[go.Table(
  header=dict(values=header, line_color='black', fill_color='white',
              align='center', font_size=16, height=30),
  cells=dict(values=[tickers, df['現在値'], df['出来高'], df['時価総額'],
             df['PER'], df['高値下落'], df['年初来'], df['１ヶ月'],
             df['１週間'], df['１日']],
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
fig.show()

df.to_csv('stock.csv')
