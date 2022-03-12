#表出力
#stock data for excel
import pandas as pd
import yahoo_fin.stock_info as si
import plotly.graph_objects as go
import datetime as datetime

#from tickers import*

# tickers_list_analysis = ['AAPL','AFRM', 'AI','AR', 'BABA', 'BIGC', 'BIIB', 'BMY',
# 'COST', 'CAT', 'COIN', 'COUR', 'CRWD', 'CVS',
# 'DDOG', 'DAL', 'DIS', 'DKNG', 'DOCS', 'DRVN', 'GDRX',
# 'EURN', 'GM', 'IAC','ICE','KOS', 'MAR', 'MAXR', 'MSFT'
# ]

tickers_list_analysis = ['FB','AAPL','MSFT','V','GOOGL','TWLO','AMZN'
]


header   = ['Ticker',
'Earnings Est(CQ)','Earnings Est(NQ)','Earnings Est(CY)','Earnings Est(NY)',
'Sales Est(CQ)','Sales Est(NQ)','Sales Est(CY)','Sales Est(NY)']
title = "Analyst Estimates (Yahoo 2021/10/25)"

#print(si.get_analysts_info('AAPL'))

df=pd.DataFrame()
for i in range(len(tickers_list_analysis)):
 data = si.get_analysts_info(tickers_list_analysis[i])
 df.loc[tickers_list_analysis[i],'Ticker']=tickers_list_analysis[i]

 earnings_est_CQ=data["Earnings Estimate"].iat[1,1]
 df.loc[tickers_list_analysis[i],'Earnings Est(CQ)']='%.2f'%(earnings_est_CQ)
 earnings_est_NQ=data["Earnings Estimate"].iat[1,2]
 df.loc[tickers_list_analysis[i],'Earnings Est(NQ)']='%.2f'%(earnings_est_NQ)
 earnings_est_CY=data["Earnings Estimate"].iat[1,3]
 df.loc[tickers_list_analysis[i],'Earnings Est(CY)']='%.2f'%(earnings_est_CY)
 earnings_est_NY=data["Earnings Estimate"].iat[1,4]
 df.loc[tickers_list_analysis[i],'Earnings Est(NY)']='%.2f'%(earnings_est_NY)

 sales_est_CQ=data["Revenue Estimate"].iat[1,1]
 df.loc[tickers_list_analysis[i],'Sales Est(CQ)']=sales_est_CQ
 sales_est_NQ=data["Revenue Estimate"].iat[1,2]
 df.loc[tickers_list_analysis[i],'Sales Est(NQ)']=sales_est_NQ
 sales_est_CY=data["Revenue Estimate"].iat[1,3]
 df.loc[tickers_list_analysis[i],'Sales Est(CY)']=sales_est_CY
 sales_est_NY=data["Revenue Estimate"].iat[1,4]
 df.loc[tickers_list_analysis[i],'Sales Est(NY)']=sales_est_NY
#print(df)

fig = go.Figure(data=[go.Table(
  header=dict(values=header, line_color='black', fill_color='white',
              align='center', font_size=16, height=30),
  cells=dict(values=[tickers_list_analysis, df['Earnings Est(CQ)'], df['Earnings Est(NQ)'],df['Earnings Est(CY)'],df['Earnings Est(NY)'],
             df['Sales Est(CQ)'],df['Sales Est(NQ)'],df['Sales Est(CY)'],df['Sales Est(NY)']],
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
fig.show()

df.to_csv('stock2.csv')
