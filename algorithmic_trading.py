import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secrets import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv('sp_500_stocks.csv')

symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
#print(data['symbol'])

price = data['latestPrice']
market_cap = data['marketCap']

my_columns = ['Ticker','Stock Price', 'Market Cap', '# of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
#print(final_dataframe)

# final_dataframe= final_dataframe.append(
#     pd.Series(
#     [
#         symbol,
#         price,
#         market_cap,
#         'N/A'
#     ],
#     index = my_columns
#     ),
#     ignore_index = True
# )
#----single line code to build panda----#
# for stock in stocks['Ticker'][:5]:
#     api_url = f'https://sandbox.iexapis.com/stable/stock/{stock}/quote/?token={IEX_CLOUD_API_TOKEN}'
#     data = requests.get(api_url).json()
#     final_dataframe = final_dataframe.append(
#         pd.Series([
#             stock,
#             data['latestPrice'],
#             data['marketCap'],
#             'N/A'
#         ],
#         index = my_columns
#         ),
#         ignore_index = True
#     )

#----Batch API can only handle 100lines----#
def chunks(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]
symbol_groups = list(chunks(stocks['Ticker'],100))
symbol_strings = []
for i in range(0,len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))
for symbol_string in symbol_strings[:1]:
    batch_api_call_url =f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol_string}&types=quote&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    for symbol in symbol_string.split(','):
        final_dataframe = final_dataframe.append(
            pd.Series([
                symbol,
                data[symbol]['quote']['latestPrice'],
                data[symbol]['quote']['marketCap'],
                'N/A'
            ],
            index = my_columns
            ),
            ignore_index = True
        )
#print(symbol_groups)
#print(final_dataframe)

portfolio_size = input('value of your portfolio: ')
try:
    val = float(portfolio_size)
    print(val)
except ValueError:
    print('please insert a number')
    portfolio_size = input('value of your portfolio: ')
    val = float(portfolio_size)

position_size = val/len(final_dataframe.index)
for i in range(0,len(final_dataframe.index)):
    final_dataframe.loc[i,'# of Shares to Buy'] = math.floor(position_size/final_dataframe.loc[i,'Stock Price'])
print(final_dataframe)
final_dataframe.to_csv('algo.csv')

writer = pd.ExcelWriter('trades.xlsx',engine='xlsxwriter')
final_dataframe.to_excel(writer,'trades',index=False)
background_color='#0a0a23'
font_color= '#ffffff'
string_format = writer.book.add_format({
    'font_color': font_color,
    'bg_color': background_color,
    'border': 1
})
dollar_format = writer.book.add_format({
    'num_format': '$0.00',
    'font_color': font_color,
    'bg_color': background_color,
    'border': 1
})
integer_format = writer.book.add_format({
    'num_format': '0',
    'font_color': font_color,
    'bg_color': background_color,
    'border': 1
})
