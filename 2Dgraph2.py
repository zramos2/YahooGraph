import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np


def next_page(url):
    value = int(url[-10:]) + 604800
    url2 = url[:-10] + str(value)
    return url2


#url = 'https://finance.yahoo.com/quote/FAS/options?date=1564704000'
# url = 'https://finance.yahoo.com/quote/FAS/options/'
url = 'https://finance.yahoo.com/quote/AMD/options?p=AMD'
r = requests.get(url)
# r = requests.get(next_page(url))

soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('.calls tbody tr')


strike = []     # Y-axis
interest = []   # X-axis
for row in rows:

    strike_price = row.select_one('.data-col2').text.strip()
    strike_price = float(strike_price)
    strike.append(strike_price)
    open_interest = row.select_one('.data-col9').text.strip()
    open_interest = int(open_interest.replace(',', ''))
    interest.append(open_interest)
"""
print(strike[0])
print(interest[0])
print(len(rows))
"""

fig = plt.figure(figsize=(9, 6))
graph = fig.add_axes([0.1, 0.1, 0.9, 0.9])
graph.scatter(interest, strike)
graph.set_xlabel('Open Interest')
graph.set_ylabel('Strike Price')
plt.show()
