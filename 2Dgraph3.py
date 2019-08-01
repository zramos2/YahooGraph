# This version reads a text file filled with stock symbols

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
# import numpy as np

"""
def find_index(array):
    index_val = []
    for i in range(len(array)):
        x = array[i] - array[i-1]
"""


# url = 'https://finance.yahoo.com/quote/FAS/options?date=1564704000'
begin_url = 'https://finance.yahoo.com/quote/'
end_url = '/options/'
textfile = open("Stock_symbols.txt", "r")
# print(textfile.read())
# print(textfile.readlines())


# total_index = []  # will be subtracted with 'indexVal' to get correct index value
actualIndx = []  # same values as 'get_index' its just outside of for loop
strike = []     # Y-axis
interest = []   # X-axis
get_title = []
numSym = 0
for line in textfile:
    numSym += 1

    url = begin_url + line.rstrip() + end_url
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('.calls tbody tr')

    get_index = 0

    for row in rows:
        strike_price = row.select_one('.data-col2').text.strip()
        strike_price = float(strike_price)
        strike.append(strike_price)
        open_interest = row.select_one('.data-col9').text.strip()
        open_interest = int(open_interest.replace(',', ''))
        interest.append(open_interest)
        get_index += 1

    actualIndx.append(get_index)
    get_title.append(line.rstrip())
#    total_index.append(len(strike))
#    print(len(strike), ' = len(strike)')
#    print(total_index, ' = total_index')
#    print(actualIndx, ' = actualIndx')
nrows = 3
ncols = 2
k = 0
fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(8, 6))

for j in range(nrows):
    for i in range(ncols):
        axs[j, i].scatter(interest[:actualIndx[k]], strike[:actualIndx[k]])
        axs[j, i].set_title(get_title[k])
        axs[j, i].set_xlabel('Open Interest')
        axs[j, i].set_ylabel('Strike Price')
        k += 1

plt.tight_layout()
plt.show()
