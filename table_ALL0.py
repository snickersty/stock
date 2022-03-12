#表出力
#stock data for excel
import pandas as pd
import yahoo_fin.stock_info as si
import plotly.graph_objects as go
#from tickers import*
tickers_list = ['DDOG', 'DAL', 'DIS', 'DKNG', 'DOCS', 'DRVN', 'GDRX',
'EURN', 'GM', 'IAC','ICE','KOS', 'MAR', 'MAXR', 'MSFT']

header   = ['Ticker', 'Close','Adj Close','Max','Min','Volume', 'Market Cap', 'GM%(CY)', 'PER','max drop',
          'YTD', '1mo', '1wk', '1d']
title = "Watchlist"
#pl = si.get_income_statement('AAPL')
pl = si.get_income_statement('AAPL')
 # df.loc[tickers_list[i],'Market Cap']=""
 # df.loc[tickers_list[i],'PER']=0
grossprofit = pl.iloc[6][0] #gross profit
sales = pl.iloc[15][0] #sales
# print(grossprofit/sales)
# print(grossprofit,sales)
print(si.get_income_statement('RBLX'))
# print(si.get_income_statement('DOCS').iloc[6])


# df=pd.DataFrame()
# for i in range(len(tickers_list)):
#  data = si.get_data(tickers_list[i])
#  df.loc[tickers_list[i],'Ticker']=tickers_list[i]

#  stk_close=data["close"].iat[-1]
#  df.loc[tickers_list[i],'Close']='%.2f'%(stk_close)

#  stk_adj=data["adjclose"].iat[-1]
#  df.loc[tickers_list[i],'Adj Close']='%.2f'%(stk_adj)

#  vol_today=data["volume"].iat[-1]
#  df.loc[tickers_list[i],'Volume']=vol_today


#  quot = si.get_quote_table(tickers_list[i], dict_result = True)
#  # df.loc[tickers_list[i],'Market Cap']=""
#  # df.loc[tickers_list[i],'PER']=0
#  if('Market Cap' in quot):
#    df.loc[tickers_list[i],'Market Cap']=quot['Market Cap']
#  if('PE Ratio (TTM)' in quot):
#    df.loc[tickers_list[i],'PER']=quot['PE Ratio (TTM)']
# sorted_df = df.sort_values(by=['Volume'], ascending=False)
# print(df, sorted_df)

# fig = go.Figure(data=[go.Table(
#   header=dict(values=header, line_color='black', fill_color='white',
#               align='center', font_size=16, height=30),
#   cells=dict(values=[tickers_list, sorted_df['Close'], sorted_df['Adj Close'],
#              sorted_df['Volume']],
#              line_color='black',
#              fill_color=[['rgb(235, 235, 235)', 'white']*(int(len(tickers_list)/2)+1)],
#              align=['center', 'right'],
#              font_size=16, height=30)
#   )],
# )

# title = title + ' ('+data.index[-1].strftime('%Y/%m/%d')+')'
# fig.update_layout(
#   title={'text': title, 'y': 0.9, 'x': 0.5},
#   font={ 'family': 'Noto Sans CJK JP', 'size': 16},
#   width=1100
# )
# #fig.show()

# sorted_df.to_csv('stock_price.csv')
