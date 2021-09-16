
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
from PIL import Image, ImageDraw, ImageFont
import datetime as datetime
import pytz
import os
import IPython
import dateutil.parser

tickers = ['GOOGL', 'AAPL', 'FB', 'AMZN', 'MSFT','TTD']



header   = ['Ticker','date', 'EPS(E)', 'EPS(ACT)', 'EPS(%)', 'Rev(E)', 'Rev(ACT)',
'Rev(%)','YoY(%)', 'Next date', 'EPS(E)', 'Rev(E)']

df = pd.DataFrame(index=tickers, columns=header)
df['Ticker']=tickers

# データ作成
for t in range(len(tickers)):
 ticker=tickers[t]
 print("\r now reading -->>  " + ticker+ "  ---" ,end="")
 url='https://www.earningswhispers.com/epsdetails/'+ticker
 site = requests.get(url)
 data = BeautifulSoup(site.text,'html.parser')

 try:
   ldate=re.sub('.*/>(.*)</.*', r'\1', str(data.find_all("div", class_="mbcontent")[0]))
   if(ldate!=''):
     last_date = dateutil.parser.parse(re.sub('.*/>(.*)</.*', r'\1', str(data.find_all("div", class_="mbcontent")[0])))
     df.loc[tickers[t],'date']=last_date.strftime('%Y/%m/%d %H:%M')

   eps_act = re.sub('.*>(.*)</.*', r'\1', str(data.find_all("div", class_="mainitem")[0])).replace('(','-').replace(')','')
   eps_est = re.sub('.*>(.*)</.*', r'\1', str(data.find_all("div", class_="thirditem")[0])).replace('(','-').replace(')','')

   if(len(data.find_all("div", class_="esurp"))>0):
     eps_sur = re.sub('.*"esurp", "(.*)", "EPS".*', r'\1', str(data.find_all("div", class_="esurp")[0]))
     df.loc[tickers[t],'EPS(%)']=eps_sur

   rev_act = re.sub('.*>(.*)</.*', r'\1', str(data.find_all("div", class_="fourthitem")[0])).replace('il','')
   rev_est = re.sub('.*>(.*)</.*', r'\1', str(data.find_all("div", class_="fifthitem")[0])).replace('il','')

   if(len(data.find_all("div", class_="rsurp"))>0):
     rev_sur = re.sub('.*"rsurp", "(.*)", "Revenue".*', r'\1', str(data.find_all("div", class_="rsurp")[0]))
     df.loc[tickers[t],'Rev(%)']=rev_sur
   else:
     df.loc[tickers[t],'Rev(%)']=''
   if(len(data.find_all("div", class_="revgrowth"))>0):
     rev_gro = re.sub('.*"revgrowth", "(.*)%",.*', r'\1%', str(data.find_all("div", class_="revgrowth")[0]))
     df.loc[tickers[t],'YoY(%)']=rev_gro
   else:
     df.loc[tickers[t],'YoY(%)']=''
   df.loc[tickers[t],'EPS(E)']=eps_est
   df.loc[tickers[t],'EPS(ACT)']=eps_act
   df.loc[tickers[t],'Rev(E)']=rev_est
   df.loc[tickers[t],'Rev(ACT)']=rev_act
   if(eps_act!='')&(eps_est!=''):
     df.loc[tickers[t],'EPS(%)']='{:.2%}'.format(float(float(eps_act.replace('$',''))-float(eps_est.replace('$','')))/abs(float(eps_est.replace('$',''))))
   else:
     df.loc[tickers[t],'EPS(%)']=''

 except:
   print("NO OLD DATA:",ticker)
   pass

 url='https://www.earningswhispers.com/stocks/'+ticker
 site = requests.get(url)
 data = BeautifulSoup(site.text,'html.parser')

 next_day  = re.sub('.*>(.*)</.*', r'\1', str(data.find_all("div", class_="mainitem")[1]))
 next_time = re.sub('.*>(.*)</.*', r'\1', str(data.find_all("div", id="earningstime")[0]))
 try:
   next_date = dateutil.parser.parse(next_day + ' ' + next_time.replace('ET',''))
 except:
   next_date = dateutil.parser.parse(next_day)
   pass
 if(last_date.strftime('%Y/%m/%d')!=next_date.strftime('%Y/%m/%d')):
   df.loc[tickers[t],'next date']=next_date.strftime('%Y/%m/%d %H:%M')
 eps_cons = re.sub('.*>Consensus:\s+(.*)</.*', r'\1', str(data.find_all("div", id="consensus")[0])).replace('(','-').replace(')','')
 rev_cons = re.sub('.*>Revenue:\s+(.*)</.*', r'\1', str(data.find_all("div", id="revest")[0])).replace('il','')
 df.loc[tickers[t],'EPS(E)']=eps_cons
 df.loc[tickers[t],'Rev(E)']=rev_cons

df = df.sort_values(['next date','date'], ascending=[True,True])
sort_tickers = list(df['Ticker'])

#########################################################################
# 表作成
#########################################################################
font_title = ImageFont.truetype("/Microsoft Yahei.ttf", 18)
font_head = ImageFont.truetype("/微软雅黑.ttf", 16)
font_txt = ImageFont.truetype("Microsoft Yahei.ttf", 16)
#########################################################################
# 初期設定
title = "ウォッチリスト決算データ"
# Xサイズ
x_width = [80,160,70,70,70,90,90,70,70,160,80,90]
y_width = 30
title_y = 50
x_buff = 10
text_color = (42,63,95)
line_color = (163,197,236)
# 色を付けたいセル（プラスは青、マイナスは赤）
cell_pct = ['EPS(%)','Rev(%)','YoY(%)','EPS(E)','EPS(ACT)','EPS(E)想']
#########################################################################
im = Image.new('RGB', (sum(x_width)+x_buff*2, y_width*(len(tickers)+1)+title_y+10), "white")
draw = ImageDraw.Draw(im)

#### タイトル 部分 ####
draw.text((sum(x_width)/2-400/2, 10),title+ ' ('+datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M")+')',
      text_color,font=font_title)

#### ヘッダー 部分 ####
xpos=x_buff
ypos=title_y
for i in range(len(header)):
 draw.rectangle([(xpos, ypos), (xpos+x_width[i], ypos+y_width)], fill=(221,237,255), outline=line_color,  width=1)
 draw.text((xpos+10, ypos+5),header[i], text_color,font=font_head)
 xpos=xpos+x_width[i]
#### データ 部分 ####
for t in range(len(sort_tickers)):
 ticker = sort_tickers[t]
 xpos=x_buff
 ypos=ypos+y_width
 for i in range(len(header)):
   draw.rectangle([(xpos, ypos), (xpos+x_width[i], ypos+y_width)], outline=line_color,  width=1
       , fill=((255,255,255) if t % 2 == 0 else (235,235,235)))

   # 色付け #########
   if(header[i] in cell_pct):
     if (str(df.loc[ticker,header[i]])[:1]=='-'):txt_color="red"
     else:txt_color="blue"
   else:
    txt_color=text_color

   draw.text((xpos+5, ypos+5),str(df.loc[ticker,header[i]]), txt_color,font=font_txt)
   xpos=xpos+x_width[i]

# 太枠形成 ##############################################################
xpos=x_buff
ypos=title_y
# 外太枠 ######################################
draw.rectangle([(xpos, ypos), (xpos+sum(x_width), ypos+y_width*(len(tickers)+1))], outline=line_color, width=2)
# ヘッダ太枠 ##################################
draw.rectangle([(xpos, ypos), (xpos+sum(x_width), ypos+y_width)], outline=line_color, width=2)
# 他太枠作成 ##################################
bold_fm='date'
bold_to='YoY(%)'
draw.rectangle([(xpos+x_width[header.index(bold_fm)-1], ypos), (xpos+sum(x_width[header.index(bold_fm)-1:header.index(bold_to)+1])
 , ypos+y_width*(len(tickers)+1))], outline=line_color, width=2)

# 出力 ##############################################################
im.save('earnings.png')
IPython.display.Image('earnings.png')
df.to_csv('earnings.csv')
#########################################################################
