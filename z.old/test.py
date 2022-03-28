#表出力
#stock data for excel
import pandas as pd
import yahoo_fin.stock_info as si
import plotly.graph_objects as go
import datetime as datetime
import sys
#from tickers import*

# print(si.get_earnings('ZKIN')['quarterly_results'])

tickers_list_analysis = ['AAPL','AFRM', 'AI','AR', 'BABA', 'BIGC', 'BIIB', 'BMY',
'COST', 'CAT', 'COIN', 'COUR', 'CRWD', 'CVS'
]

# tickers_list_analysis = ['DDOG', 'DAL', 'DIS', 'DKNG', 'DOCS', 'DRVN', 'GDRX',
# 'EURN', 'GM', 'IAC','ICE','KOS', 'MAR', 'MAXR', 'MSFT']
#
# tickers_list_analysis = [
# 'NKE', 'NFLX', 'OKTA', 'PFE', 'PG', 'PYPL',
# 'REGN', 'RBLX','RPRX', 'SEER', 'SPCE', 'SBLK',
# 'TSLA', 'TSM', 'TTD', 'TWLO', 'U', 'UPST']

# tickers_list_analysis = ['V', 'VALE', 'VLDR', 'XMTR', 'ZM','ZKIN']
#,
header   = ['Ticker',
'Sales','Op Income%','Net Income','EPS','OpCF']
title = "Analyst Estimates (Yahoo 2021/10/25)"


df=pd.DataFrame()
column = 2
for i in range(len(tickers_list_analysis)):
 data = si.get_financials(tickers_list_analysis[i])
 df.loc[tickers_list_analysis[i],'Ticker']=tickers_list_analysis[i]

 sales=data["quarterly_income_statement"].loc['totalRevenue'][column]
 df.loc[tickers_list_analysis[i],'Sales']='%.2f'%(sales/1000000000)

 if sales > 0:
     opincome=data["quarterly_income_statement"].loc['operatingIncome'][column]
     df.loc[tickers_list_analysis[i],'Op Income%']='{:.2%}'.format((opincome/sales))

 netincome=data["quarterly_income_statement"].loc['netIncome'][column]
 df.loc[tickers_list_analysis[i],'Net Income']='%.2f'%(netincome/1000000000)

 try:
     eps = si.get_earnings(tickers_list_analysis[i])['quarterly_results'].iat[-1-column,1]
     #print(tickers_list_analysis[i], eps)
     df.loc[tickers_list_analysis[i],'EPS']='%.2f'%(eps)
 except:
     pass

 cf=data['quarterly_cash_flow'].loc['totalCashFromOperatingActivities'][column]
 df.loc[tickers_list_analysis[i],'OpCF']='%.2f'%(cf/1000000000)

fig = go.Figure(data=[go.Table(
  header=dict(values=header, line_color='black', fill_color='white',
              align='center', font_size=16, height=30),
  cells=dict(values=[tickers_list_analysis, df['Sales'], df['Op Income%'], df['Net Income'], df['EPS'], df['OpCF']],
             line_color='black',
             fill_color=[['rgb(235, 235, 235)', 'white']*(int(len(tickers_list_analysis)/2)+1)],
             align=['center', 'right'],
             font_size=16, height=30)
  )],
)

fig.update_layout(
  title={'text': title, 'y': 0.9, 'x': 0.5},
  font={ 'family': 'Noto Sans CJK JP', 'size': 16},
  width=1100
)
#fig.show()

df.to_csv('stock_financials.csv')
