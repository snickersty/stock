#表出力
#stock data for excel
import pandas as pd
import yahoo_fin.stock_info as si
import plotly.graph_objects as go
#from tickers import*
tickers_list = ['AAPL','ABNB','AFRM', 'AI','AR', 'ARCB', 'BABA', 'BIGC', 'BIIB', 'BMY',
'CAT','CCL','COST',  'COIN', 'COUR', 'CRWD', 'CVS',
'DDOG', 'DAL', 'DIS', 'DKNG', 'DOCN','DOCS', 'DRVN', 'ENPH','EURN','FCX','GDRX', 'GM','GOOGL',
'IAC','ICE','INMD','KOS', 'MAR', 'MAXR', 'MQ','MSFT','MTDR','MTTR','MU',
'NET', 'NKE', 'NFLX', 'NVDA', 'NTR','OKTA','ONON', 'PFE', 'PG', 'PLTR','PYPL',
'QCOM','RDWR','REGN', 'RIVN', 'RBLX','RPRX', 'SBLK','SEER','SEMR', 'SPCE', 'SQ',
'TSLA', 'TSM', 'TTD', 'TWLO', 'U', 'UPST','WST',
'V', 'VALE', 'VLDR', 'XMTR', 'ZM','ZKIN',
'SPXS','GLD','HDV','SPYD','VYM','MGV','DIA','QQQ','VAW','VDE','VT','VTI','VWO','XLE',
'EWY','TUR','ACWI','GLIN','FXI','EWZ','EWW','EPOL']
#
header   = ['Ticker', 'Close12_2','Close12','Close11','Close10','Close9','Close8',
'Close7','Close6','Close5','Close4','Close3','Close2','Close1']
title = "Watchlist"
#print(si.get_data('AAPL'))

df=pd.DataFrame()
for i in range(len(tickers_list)):
  #print(tickers_list[i])
  data = si.get_data(tickers_list[i])
  df.loc[tickers_list[i],'Ticker']=tickers_list[i]

  stk_close=data["close"].iat[-1]
  df.loc[tickers_list[i],'Close12']='%.2f'%(stk_close)

  if '2020-12-31' in data.index:
    stk_yend=data.loc['2020-12-31','close']
    df.loc[tickers_list[i],'Close12_2']='%.2f'%(stk_yend)
    print('12',stk_yend)
  if '2021-01-29' in data.index:
    stk_yend=data.loc['2021-01-29','close']
    df.loc[tickers_list[i],'Close1']='%.2f'%(stk_yend)
    print('1',stk_yend)
  if '2021-02-26' in data.index:
    stk_yend=data.loc['2021-02-26','close']
    df.loc[tickers_list[i],'Close2']='%.2f'%(stk_yend)
    print('2',stk_yend)
  if '2021-03-31' in data.index:
    stk_yend=data.loc['2021-03-31','close']
    df.loc[tickers_list[i],'Close3']='%.2f'%(stk_yend)
    print('3',stk_yend)
  if '2021-04-30' in data.index:
    stk_yend=data.loc['2021-04-30','close']
    df.loc[tickers_list[i],'Close4']='%.2f'%(stk_yend)
    print('4',stk_yend)
  if '2021-05-28' in data.index:
    stk_yend=data.loc['2021-05-28','close']
    df.loc[tickers_list[i],'Close5']='%.2f'%(stk_yend)
    print('5',stk_yend)
  if '2021-06-30' in data.index:
    stk_yend=data.loc['2021-06-30','close']
    df.loc[tickers_list[i],'Close6']='%.2f'%(stk_yend)
  if '2021-07-30' in data.index:
    stk_yend=data.loc['2021-07-30','close']
    df.loc[tickers_list[i],'Close7']='%.2f'%(stk_yend)
  if '2021-08-31' in data.index:
    stk_yend=data.loc['2021-08-31','close']
    df.loc[tickers_list[i],'Close8']='%.2f'%(stk_yend)
  if '2021-09-30' in data.index:
    stk_yend=data.loc['2021-09-30','close']
    df.loc[tickers_list[i],'Close9']='%.2f'%(stk_yend)
  if '2021-10-29' in data.index:
    stk_yend=data.loc['2021-10-29','close']
    df.loc[tickers_list[i],'Close10']='%.2f'%(stk_yend)
  if '2021-11-30' in data.index:
    stk_yend=data.loc['2021-11-30','close']
    df.loc[tickers_list[i],'Close11']='%.2f'%(stk_yend)
  if '2021-12-31' in data.index:
    stk_yend=data.loc['2021-12-31','close']
    df.loc[tickers_list[i],'Close12']='%.2f'%(stk_yend)







fig = go.Figure(data=[go.Table(
  header=dict(values=header, line_color='black', fill_color='white',
              align='center', font_size=16, height=30),
  cells=dict(values=[df['Ticker'], df['Close12'], df['Close11'], 
             df['Close10'],df['Close9'], df['Close8'], df['Close7'],
             df['Close6'], df['Close5'], df['Close4'],
             df['Close3'], df['Close2'], df['Close1']],
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
df.to_csv('stock_price_2021.csv')
