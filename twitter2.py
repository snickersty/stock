#TYedit twitter
#version of NON PANDA, use DICTIONARY
import datetime as datetime
#import datetime as date
from datetime import timedelta
import matplotlib.pyplot as plt
import pandas as pd
import yahoo_fin.stock_info as si
import numpy as np

#{tickers {date, close, adj close}}




#create base dictionary with tickers
def create_dict(int_tickers):
    stock_dict={}
    for i in range(len(int_tickers)):
        if i not in stock_dict:
            stock_dict[int_tickers[i]] = {}
    return stock_dict


#print(dict_etf)

#date to track daily variance %
yesterday = (datetime.datetime.today() - datetime.timedelta(days =1)).strftime('%Y-%m-%d')
today = (datetime.datetime.today() - datetime.timedelta(days =0)).strftime('%Y-%m-%d')
#today = datetime.datetime.today().strftime('%Y-%m-%d')
#print((si.get_data('VTI', start_date=yesterday)['close']))
print(today)

#populate DICTIONARY
def popu_dict(dict, int_tickers):
    for i in range(len(int_tickers)):
        dict[int_tickers[i]]['close'] = (si.get_data(int_tickers[i], start_date=yesterday)['close']).tolist()
        dict[int_tickers[i]]['adjclose'] = (si.get_data(int_tickers[i], start_date=yesterday)['adjclose']).tolist()
    return(dict)

#print('popu',popu_dict(dict_etf,ext_tickers))
    #print(stock_dict)
    #print(stock_dict['VTI']['close'][0])


# 上昇率を追加
def var_dict(dict, int_tickers):
    for i in range(len(int_tickers)):
        #前日比
        variance = (dict[int_tickers[i]]['close'][1]/dict[int_tickers[i]]['close'][0]-1)*100
        per='%.2f'%(variance)
        per='↑'+per if (per[:1]!='-') else '↓'+ per[1:]
        dict[int_tickers[i]]['var'] = per
    return(dict)

#
# ACTIVE
active_tickers = (si.get_day_most_active().iloc[0:4,0].tolist())
dict_active = create_dict(active_tickers)
dict_active = popu_dict(dict_active,active_tickers)
dict_active = var_dict(dict_active,active_tickers)
print(dict_active)
dict_active_key = list(dict_active)

ext_tickers = ['DIA','QQQ','VTI']
dict_etf = create_dict(ext_tickers)
dict_etf = popu_dict(dict_etf,ext_tickers)
dict_etf = var_dict(dict_etf,ext_tickers)
date = datetime.datetime.today()
# #print(list(df.columns.values)[0])
#
#
#
print(str(date.month) +'月'+str(date.day)+'日マーケット振り返り♫' +'\n'+
'Top Active: $'+ dict_active_key[0]+ ' ' + dict_active[dict_active_key[0]]['var']+ '%; $'
+ dict_active_key[1]+ ' ' + dict_active[dict_active_key[1]]['var']+'%; $'
+ dict_active_key[2]+ ' ' + dict_active[dict_active_key[2]]['var']+'%; $'
+ dict_active_key[3]+ ' ' + dict_active[dict_active_key[3]]['var']+'%; '
+ '\n'+'今日は雇用統計予想より大幅に小さく、10YRも2％以上上昇'+'\n'+
'$DIA ' + dict_etf['DIA']['var']+'% '+'$QQQ ' + dict_etf['QQQ']['var']+'% '+'$VTI ' + dict_etf['VTI']['var']+'%\n'+
'#投資家さんと繋がりたい')
