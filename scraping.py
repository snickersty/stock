from bs4 import BeautifulSoup
import requests

url = 'https://finance.yahoo.com/gainers'
site = requests.get(url)
data = BeautifulSoup(site.text,'html.parser')
title = data.find('title').get_text()
print(title)
print(data)
