#TYedit twitter
#version of NON PANDA, use DICTIONARY
import datetime as datetime
from datetime import date
from datetime import timedelta
import datetime
import matplotlib.pyplot as plt
import yahoo_fin.stock_info as si
import numpy as np
import calendar

today_date = datetime.datetime.today()
#print(today_date.month)
week_action = 0
month_action = 0
month_end = calendar.monthrange(today_date.year,today_date.month)[1]
date = datetime.datetime.today()


##########Check Date and Set ACTION##########
#if it's a monday compare to 3 days ago, friday
if date.today().weekday() == 0:
    print('monday')
    yesterday = (datetime.datetime.today() - datetime.timedelta(days =3)).strftime('%Y-%m-%d')
    try:
        si.get_data('QQQ', start_date=yesterday)['close']
    except KeyError:
        yesterday = (datetime.datetime.today() - datetime.timedelta(days =4)).strftime('%Y-%m-%d')

#if it's a friday, do 1week analysis as well
elif date.today().weekday() == 4:
    print('friday')
    week_action = 1
    yesterday = (datetime.datetime.today() - datetime.timedelta(days =1)).strftime('%Y-%m-%d')
    week = (datetime.datetime.today() - datetime.timedelta(days =7)).strftime('%Y-%m-%d')

#if NOT Monday & appointed delta is NA, check another weekday
elif date.today().weekday() != 0:
    print('non-monday')
    yesterday = (datetime.datetime.today() - datetime.timedelta(days =1)).strftime('%Y-%m-%d')
    try:
        si.get_data('QQQ', start_date=yesterday)['close']
    except KeyError:
        yesterday = (datetime.datetime.today() - datetime.timedelta(days =4)).strftime('%Y-%m-%d')

print(yesterday)

##########FLAG month-end#########
# print(datetime.datetime.today())
# today_date1 = (datetime.datetime.today() - datetime.timedelta(days =21))
# today_date = (datetime.datetime.today() - datetime.timedelta(days =21)).strftime('%d')
# print(today_date)

# if int(today_date) == 28:
#     month_action = 1
#     last_month = (today_date1 - datetime.timedelta(days = 28)).strftime('%Y-%m-%d')
#     print(last_month)

if date.day == month_end:
    month_action = 1
    month = (datetime.datetime.today() - datetime.timedelta(days = month_end)).strftime('%Y-%m-%d')
elif date.today().weekday() == 4:
    if date.day + 1 == month_end:
        month_action = 1
        month = (datetime.datetime.today() - datetime.timedelta(days = date.day)).strftime('%Y-%m-%d')
    if today_date.day + 2 == month_end:
        month_action = 1
        month = (datetime.datetime.today() - datetime.timedelta(days = date.day)).strftime('%Y-%m-%d')
    


##########ALL: create base dictionary with tickers#########
def create_dict(int_tickers):
    stock_dict={}
    for i in range(len(int_tickers)):
        if i not in stock_dict:
            stock_dict[int_tickers[i]] = {}
    return stock_dict
#print(dict_etf)

##########DAY: populate DICTIONARY with from YESTERDAY's CLOSE price
def popu_dict_day(dict, int_tickers):
    for i in range(len(int_tickers)):
        dict[int_tickers[i]]['close'] = (si.get_data(int_tickers[i], start_date=yesterday)['close']).tolist()
    return(dict)

##########ALL:上昇率を追加
def var_dict(dict, int_tickers):
    for i in range(len(int_tickers)):
        #前日比
        print(dict[int_tickers[i]]['close'])
        previous = dict[int_tickers[i]]['close'][0]
        today = dict[int_tickers[i]]['close'][-1]
        variance = (today/previous-1)*100
        
        per='%.2f'%(variance)
        per='↑'+per if (per[:1]!='-') else '↓'+ per[1:]
        dict[int_tickers[i]]['var'] = per
    return(dict)


########DAILY ACTION########
# ACTIVE
active_tickers = (si.get_day_most_active().iloc[0:4,0].tolist())
dict_active = create_dict(active_tickers)
dict_active = popu_dict_day(dict_active,active_tickers)
dict_active = var_dict(dict_active,active_tickers)
#print('active',active_tickers)
dict_active_key = list(dict_active)
#print('active2',dict_active)


ext_tickers = ['DIA','QQQ','VTI']
dict_etf = create_dict(ext_tickers)
#print(dict_etf)
dict_etf = popu_dict_day(dict_etf,ext_tickers)
dict_etf = var_dict(dict_etf,ext_tickers)

#print(dict_etf)

print(str(date.month) +'月'+str(date.day)+'日マーケット振り返り♫' +'\n'+
'Top Active: $'+ dict_active_key[0]+ ' ' + dict_active[dict_active_key[0]]['var']+ '%; $'
+ dict_active_key[1]+ ' ' + dict_active[dict_active_key[1]]['var']+'%; $'
+ dict_active_key[2]+ ' ' + dict_active[dict_active_key[2]]['var']+'%; $'
+ dict_active_key[3]+ ' ' + dict_active[dict_active_key[3]]['var']+'%; '
+ '\n'+'今日は'+'\n'+
'$DIA ' + dict_etf['DIA']['var']+'% '+'$QQQ ' + dict_etf['QQQ']['var']+'% '+'$VTI ' + dict_etf['VTI']['var']+'%\n'+
'#投資家さんと繋がりたい')


#########WEEKLY ACTION########
if week_action == 1:
    def popu_dict_week(dict, int_tickers):
        for i in range(len(int_tickers)):
            dict[int_tickers[i]]['close'] = (si.get_data(int_tickers[i], start_date=week)['close']).tolist()
        return(dict)
    

    ext_tickers = ['^TNX','DIA','QQQ','VTI','IWM','VWO','VIS','VAW','VCR','VDE','VFH','VNQ','GLD','BTC-USD']
    dict_etf = create_dict(ext_tickers)
    dict_etf = popu_dict_week(dict_etf,ext_tickers)
    dict_etf = var_dict(dict_etf,ext_tickers)
    #print(print(dict_etf['DIA']['close'][-6:]))

    #yesterday = (datetime.datetime.today() - datetime.timedelta(days =0))

    print(str(date.month) +'月'+str(date.day)+'日週振返り♫' +'\n'+
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


#########MONTHLY ACTION########
########Make sure last month start date isnt a weekend########

month_end = calendar.monthrange(today_date.year,today_date.month)[1]
last_month = (datetime.datetime.today() - datetime.timedelta(days = month_end)).strftime('%Y-%m-%d')
print(last_month)
if date.last_month().weekday() == 5:
    last_month = (datetime.datetime.today() - datetime.timedelta(days = month_end+1)).strftime('%Y-%m-%d')
elif date.last_month().weekday() == 6:
    last_month = (datetime.datetime.today() - datetime.timedelta(days = month_end+2)).strftime('%Y-%m-%d')

print(month)
if month_action == 0 :
    ########Month Variance########
    def popu_dict_month(dict, int_tickers):
        for i in range(len(int_tickers)):
            dict[int_tickers[i]]['close'] = (si.get_data(int_tickers[i], start_date=last_month)['close']).tolist()
        return(dict)
    
    ext_tickers = ['^TNX','DIA','QQQ','VTI','IWM','VWO','VIS','VAW','VCR','VDE','VFH','VNQ','GLD','BTC-USD']
    dict_etf = create_dict(ext_tickers)
    dict_etf = popu_dict_month(dict_etf,ext_tickers)
    print(dict_etf["DIA"])
    print(sum(len(v) for v in dict_etf['DIA'].values()))
    print(dict_etf["DIA"]["close"][-1])
    dict_etf = var_dict(dict_etf,ext_tickers)
    print(print(dict_etf['DIA']['close'][-6:]))

    print(str(date.month) +'月'+str(date.day)+'週振返り♫' +'\n'+
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

    ########YTD Variance########
    def popu_dict_ytd(dict, int_tickers):
        for i in range(len(int_tickers)):
            dict[int_tickers[i]]['close'] = (si.get_data(int_tickers[i], start_date=2021-12-31)['close']).tolist()
        return(dict)
    

    dict_etf = create_dict(ext_tickers)
    dict_etf = popu_dict_ytd(dict_etf,ext_tickers)
    dict_etf = var_dict(dict_etf,ext_tickers)

    print(str(date.month) +'月'+str(date.day)+'年初来♫' +'\n'+
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
