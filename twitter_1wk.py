#TYedit twitter
#version of NON PANDA, use DICTIONARY
import datetime as datetime
#import datetime as date
from datetime import timedelta
import matplotlib.pyplot as plt
import pandas as pd
import yahoo_fin.stock_info as si
import numpy as np


#create base dictionary with tickers
def create_dict(int_tickers):
    stock_dict={}
    for i in range(len(int_tickers)):
        if i not in stock_dict:
            stock_dict[int_tickers[i]] = {}
    return stock_dict


#date to track daily variance %
week1 = (datetime.datetime.today() - datetime.timedelta(days =8)).strftime('%Y-%m-%d')
week2 = (datetime.datetime.today() - datetime.timedelta(days =7)).strftime('%Y-%m-%d')
today = datetime.datetime.today().strftime('%Y-%m-%d')
#print((si.get_data('VTI', start_date=yesterday)['close']))
print(today)

#populate DICTIONARY
def popu_dict(dict, int_tickers):
    for i in range(len(int_tickers)):
        dict[int_tickers[i]]['close'] = (si.get_data(int_tickers[i], start_date=week1)['close']).tolist()
    return(dict)


# 上昇率を追加
def var_dict(dict, int_tickers):
    for i in range(len(int_tickers)):
        #前日比
        if int_tickers[i] == '^TNX':
            variance = (dict[int_tickers[i]]['close'][-1]/dict[int_tickers[i]]['close'][-7]-1)*100
            per='%.2f'%(variance)
            per='↑'+per if (per[:1]!='-') else '↓'+ per[1:]
            dict[int_tickers[i]]['var'] = per
        else:
            variance = (dict[int_tickers[i]]['close'][-1]/dict[int_tickers[i]]['close'][-6]-1)*100
            per='%.2f'%(variance)
            per='↑'+per if (per[:1]!='-') else '↓'+ per[1:]
            dict[int_tickers[i]]['var'] = per
    return(dict)

ext_tickers = ['^TNX','DIA','QQQ','VTI','IWM','VWO','VIS','VAW','VCR','VDE','VFH','VNQ','GLD','BTC-USD']
dict_etf = create_dict(ext_tickers)
dict_etf = popu_dict(dict_etf,ext_tickers)
dict_etf = var_dict(dict_etf,ext_tickers)
yesterday = (datetime.datetime.today() - datetime.timedelta(days =1))
#print(dict_etf['^TNX']['close'][-6])
#print(dict_etf['^TNX']['close'][-1])

print(str(yesterday.month) +'月'+str(yesterday.day)+'日週マーケット振り返り♫' +'\n'+
'10YR '+ dict_etf['^TNX']['var']+'%\n'+
'$DIA ' + dict_etf['DIA']['var']+'% '+'$QQQ ' + dict_etf['QQQ']['var']+'% '+'$VTI ' + dict_etf['VTI']['var']+'%\n'+
'IWM(Russ2000) '+ dict_etf['IWM']['var']+'%\n'+
'VWO(新興国) '+ dict_etf['VWO']['var']+'%\n'+
'VIS(資本) '+ dict_etf['VIS']['var']+'%\n'+
'VAW(素材) '+ dict_etf['VAW']['var']+'%\n'+
'VCR(一般消費) '+ dict_etf['VCR']['var']+'%\n'+
'VDE(エネルギー) '+ dict_etf['VDE']['var']+'%\n'+
'VFH(金融) '+ dict_etf['VFH']['var']+'%\n'+
'VNQ(不動産) '+ dict_etf['VNQ']['var']+'%\n'+
'GLD '+ dict_etf['GLD']['var']+'%\n'+
'BTC '+ dict_etf['BTC-USD']['var']+'%\n'+
'#投資家さんと繋がりたい')
