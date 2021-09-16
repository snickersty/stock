#TYedit twitter
import datetime as datetime
import datetime as date
import matplotlib.pyplot as plt
import pandas as pd
import yahoo_fin.stock_info as si
import numpy as np


tickers = ['DIA','QQQ','VTI']
start=datetime.datetime(2021,9,3)
print(datetime.datetime.today().strftime('%Y-%m-%d'))
stop=datetime.datetime(2021,9,8)
df = pd.DataFrame()
#print(df)


for i in range(len(tickers)):
 data = si.get_data(tickers[i], start_date=start, end_date=stop)['close']
 df=pd.concat([df, data], axis=1)
 df.rename(columns={'close': tickers[i]}, inplace=True)
#print(df)

# plt.style.use('ggplot')
# fig = plt.figure(figsize=(4,4))
# ax = fig.add_subplot(111)
df=(df/df.iloc[0]-1)*100
df.sort_values(df.index[-1],axis=1,inplace=True)
#print('test',df)

# ラベルに上昇率を追加
for i in range(len(df.columns)):
 per='%.2f'%((df[df.columns[i]].iloc[-1]))
 per='↑'+per if (per[:1]!='-') else '↓'+per
 df.rename(columns={df.columns[i]: ('$')+df.columns[i]+' '+per}, inplace=True)
df = df.reindex(sorted(df.columns), axis=1)
#print(df.replace('-',''),'1')

#WINNERS & LOSERS
gainers = si.get_day_gainers(count=2)
losers = si.get_day_losers(count=2)
gainers_ticker = (gainers['Symbol'])
gainers_name = (gainers['Name'])
#print(gainers_ticker[0])

#WINNERS
df_gainers = pd.DataFrame()
for i in range(len(gainers_ticker)):
 data = si.get_data(gainers_ticker[i], start_date=start, end_date=stop)['close']
 df_gainers=pd.concat([df_gainers, data], axis=1)
 df_gainers.rename(columns={'close': gainers_ticker[i]}, inplace=True)
df_gainers=(df_gainers/df_gainers.iloc[0]-1)*100
df_gainers.sort_values(df_gainers.index[-1],axis=1,inplace=True)
#print(df_gainers)

#WINNERS ラベルに上昇率を追加
for i in range(len(df_gainers.columns)):
 per='%.0f'%((df_gainers[df_gainers.columns[i]].iloc[-1]))
 per='+'+per if (per[:1]!='-') else per
 df_gainers.rename(columns={df_gainers.columns[i]: ('$')+df_gainers.columns[i]+' '+per}, inplace=True)
df_gainers = df_gainers.reindex(sorted(df_gainers.columns), axis=1)
print(df_gainers)

date = datetime.datetime.today()
#print(list(df.columns.values)[0])



print(str(date.month) +'月'+str(date.day)+'日マーケット振り返り♫' +'\n'+
'Top Winners: Innate Pharma $IPHA (+45%); Vera Therapeutics $VERA (+32%)'+'\n'+
'Top Losers: Forte Biosciences $FBRX (-82%); Sphere 3D $ANY (-32%)'+'\n'+
'今日は雇用統計予想より大幅に小さく、10YRも2％以上上昇'+'\n'+
list(df.columns.values)[0]+' '+list(df.columns.values)[1]+' '+list(df.columns.values)[2]+'\n'+
'#投資家さんと繋がりたい')
