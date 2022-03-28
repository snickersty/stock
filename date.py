######SET DATE FOR TWITTER COMMENT & HEATMAP######
import datetime as datetime
from datetime import date
from datetime import timedelta
import datetime
import calendar
import yahoo_fin.stock_info as si

today_date = datetime.datetime.today()
date = datetime.datetime.today()
today_yyyy = int(today_date.strftime('%Y'))
today_mm = int(today_date.strftime('%m'))
today_dd = int(today_date.strftime('%d'))
print(today_date)

month_end_dd = calendar.monthrange(today_date.year,today_date.month)[1]

last_month = (datetime.datetime.today() - datetime.timedelta(days =int(today_dd)))
last_month_yyyy = int(last_month.strftime('%Y'))
last_month_mm = int(last_month.strftime('%m'))
last_month_dd = int(last_month.strftime('%d'))


weekday_today = datetime.date(today_yyyy, today_mm, today_dd).weekday()
weekday_last_month = datetime.date(last_month_yyyy, last_month_mm, last_month_dd).weekday()
print(weekday_last_month)

yesterday = 0
week_yesterday = 0
month_yesterday = 0

week_action = 0
month_action = 0


##########Check Date and Set ACTION##########
#if it's a monday compare to 3 days ago, friday
if weekday_today == 0:
    print('monday')
    yesterday = (datetime.datetime.today() - datetime.timedelta(days =3)).strftime('%Y-%m-%d')
    try:
        si.get_data('QQQ', start_date=yesterday)['close']
    except KeyError:
        yesterday = (datetime.datetime.today() - datetime.timedelta(days =4)).strftime('%Y-%m-%d')

#if it's a friday, do 1week analysis as well
elif weekday_today == 4:
    print('friday')
    week_action = 1
    yesterday = (datetime.datetime.today() - datetime.timedelta(days =1)).strftime('%Y-%m-%d')
    week_yesterday = (datetime.datetime.today() - datetime.timedelta(days =7)).strftime('%Y-%m-%d')

#if NOT Monday & appointed delta is NA, check another weekday
elif weekday_today != 0:
    print('non-monday')
    yesterday = (datetime.datetime.today() - datetime.timedelta(days =1)).strftime('%Y-%m-%d')
    try:
        si.get_data('QQQ', start_date=yesterday)['close']
    except KeyError:
        yesterday = (datetime.datetime.today() - datetime.timedelta(days =2)).strftime('%Y-%m-%d')

print('yesterday',yesterday)


##########FLAG month-end#########
# if month end is wkday
if today_dd == month_end_dd:
  month_action = 1

elif ( today_dd == month_end_dd -2) and (weekday_today == 4):
  month_action = 1

elif ( today_dd == month_end_dd -1) and (weekday_today == 4):
  month_action = 1

try:
      si.get_data('QQQ', start_date=last_month.strftime('%Y-%m-%d'))['close']
except KeyError:
    last_month = (datetime.datetime.today() - datetime.timedelta(days =today_dd+1)).strftime('%Y-%m-%d')
try:
    si.get_data('QQQ', start_date=last_month.strftime('%Y-%m-%d'))['close']
except KeyError:
    last_month = (datetime.datetime.today() - datetime.timedelta(days =today_dd+2)).strftime('%Y-%m-%d')