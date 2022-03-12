#heatmap 1DAY

import pandas as pd
from math import floor, ceil
import yahoo_fin.stock_info as si
import japanize_matplotlib
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import IPython
import datetime as datetime
import pytz
import os
from tickers import*

# # 1day #####
# diff_day = 1
# max_per = 3 # maxのパーセンテージ (for coloring level)
## 1week #####
diff_day  = 5
last_week = (datetime.datetime.today() - datetime.timedelta(diff_day)).strftime('%Y-%m-%d')
max_per  = 6 # maxのパーセンテージ
## 1month ##### #diff_day  = 22 #max_per  = 10 # maxのパーセンテージ

x_size = 8 # 横に表示する最大数
##### 初期設定　ここまで ##################

x_width = 90
y_width = 75

def get_rgb(limit, value):
 if(value<=-limit): return (246,53,56)
 if(value<=(-limit+0.02)): return (191,64,69)
 if(value<=(-limit+0.04)): return (139,68,78)
 if(value>=limit): return (48,204,90)
 if(value>=(limit-0.02)): return (47,158,79)
 if(value>=(limit-0.04)): return (53,118,78)
 if(value==0): return (65,69,84)
 if(np.isnan(value)): return (65,69,84)
 color_list = sns.diverging_palette(12, 150, sep=1, n=100, center="dark")
 rgb=color_list[50+int(value/limit*50)]
 return (int(rgb[0]*255*1.5),int(rgb[1]*255*1.5),int(rgb[2]*255*1.5))

font_title = ImageFont.truetype("/font/kurobara-gothic-bold.ttf", 25)
font_name = ImageFont.truetype("/font/Microsoft Yahei.ttf", 12)
font_cate = ImageFont.truetype("/font/微软雅黑.ttf", 16)
font_ticker = ImageFont.truetype("/font/FrutigerLTStd-ExtraBlackCn.otf", 16)
font_pct = ImageFont.truetype("/font/PTC55F.ttf", 12)


y_size=0
for name in categ.keys():
 y_size=y_size+ceil(len(categ[name])/x_size)

im = Image.new('RGB', (x_width*x_size, y_width*y_size+42*len(categ)), (54,49,70))
draw = ImageDraw.Draw(im)

y_pos=0
draw.rectangle([(0, y_pos), (x_width*x_size, y_pos+50)], fill=(250,250,200))
y_pos = 50
for name in categ.keys():
  x_pos=0
  draw.rectangle([(0, y_pos), (x_width*x_size, y_pos+30)], fill=(250,250,138), outline=(38,41,49))
  draw.text((x_pos+10, y_pos+5),name,'black',font=font_cate)
  y_pos=y_pos+30
  for ticker in categ[name].keys():
    #print(ticker)
    data = si.get_data(ticker)["close"]
    data_pct=data.pct_change(diff_day)

    stock='${:,.2f}'.format(data.iat[-1])
    pct=data_pct.iat[-1]
    chgpct='{:.2%}'.format(pct)
    if chgpct[:1]!='-': chgpct='+'+chgpct

    draw.rectangle([(x_pos, y_pos), (x_pos+x_width, y_pos+y_width)], fill=get_rgb(max_per/100,pct), outline=(38,41,49))
    draw.text((x_pos+20, y_pos+5), ticker,'white',font=font_ticker)
    draw.text((x_pos+8, y_pos+23), categ[name][ticker][:10],'white',font=font_name)
    draw.text((x_pos+20, y_pos+40), stock, 'white',font=font_pct)
    draw.text((x_pos+20, y_pos+55), chgpct, 'white',font=font_pct)

    x_pos=x_pos+x_width
    if((x_pos+x_width)>x_width*x_size)|(ticker==list(categ[name].keys())[-1]):
      x_pos=0
      y_pos=y_pos+y_width
draw.text((x_width*x_size-490, 10),'***本日のヒートマップ***','black',font=font_title)
draw.text((x_width*x_size-100, 15),'@snickersty','black',font=font_cate)
draw.text((x_width*x_size-150, 55),datetime.datetime.now(pytz.timezone('America/New_York')).strftime('１週間 '+"%Y/%m/%d"),'black',font=font_cate)

if not os.path.isdir('/'): os.makedirs('/')
im.save('1wk.png')
IPython.display.Image('1wk.png')
