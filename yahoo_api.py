import yfinance as yf
import datetime as datatime
from datetime import datetime
from datetime import timedelta
from datetime import date
import pandas as pd

msft = yf.Ticker("MSFT")
#print(msft.history(period="1mo"))

# get stock info
#print(msft.info)

# get historical market data
#hist = msft.history(period="5d")
#print(hist)

# /** USE for updating excel **/
#data_df = yf.download('AFRM AAPL AI BABA BIGC BIIB BMY COST CAT COIN COUR CRWD CVS DDOG DAL DIS DKNG DOCS DRVN GDRX EURN GM KOS MAR MAXR MSFT NKE NFLX OKTA PFE PG PYPL REGN RBLX SEER SPCE SBLK TSLA TSM TTD TWLO U V VALE VLDR XMTR ZM', columns='adj close', start="2021-07-28", end="2021-08-31", interval = "1m")
#print(data_df)
#data_df = data_df['adjclose']
#data_df.to_csv('stock.csv')

stocks = ['AFRM', 'AAPL', 'AI', 'BABA', 'BIGC', 'BIIB', 'BMY', 'COST', 'CAT', 'COIN', 'COUR', 'CRWD', 'CVS', 'DDOG', 'DAL', 'DIS', 'DKNG', 'DOCS', 'DRVN', 'GDRX', 'EURN', 'GM', 'KOS', 'MAR', 'MAXR', 'MSFT', 'NKE', 'NFLX', 'OKTA', 'PFE', 'PG', 'PYPL', 'REGN', 'RBLX', 'SEER', 'SPCE', 'SBLK', 'TSLA', 'TSM', 'TTD', 'TWLO', 'U', 'V', 'VALE', 'VLDR', 'XMTR', 'ZM']
df = pd.DataFrame()

today = datetime.now().date().strftime('%Y-%m-%d')
yesterday = datetime.now() - timedelta(1)
yesterday = datetime.strftime(yesterday, '%Y-%m-%d')

for stock in stocks:
    output = yf.Ticker(stock).history(start='2021-08-25', end=today).Close
    print(output,stock)
    output.to_csv('stock.csv')

for i in range(len(stocks)):
 data = si.get_data(stocks[i])
 df.loc[stocks[i],'Ticker']=stocks[i]
