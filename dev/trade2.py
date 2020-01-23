#!/usr/bin/env python
# This version reads in an input as a stock symbol
# August 24, 2019

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
# import numpy as np

# url = 'https://finance.yahoo.com/quote/FAS/options?date=1564704000'
begin_url = 'https://finance.yahoo.com/quote/'
end_url = '/options/'

stock_symbol = ""
while(stock_symbol != 'ZZZ'):
    stock_symbol = input("Enter a stock symbol: ")
    if stock_symbol == 'ZZZ':
        break
    print(stock_symbol)
    url = begin_url + stock_symbol + end_url
    print(url)

    r = requests.get(url)
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

print("Input = 'ZZZ' Ending loop. ")
