from mpl_toolkits.mplot3d import Axes3D
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np


def get_webpages(url):
    links = []
    for i in range(3):
        value = int(url[-10:]) + (i * 604800)
        url2 = url[:-10] + str(value)
        links.append(url2)
    return links


def get_dates(url):
    website = soup.select_one('.qsp-2col-options div span')
    website1 = website.find_next_sibling('span').find_next_sibling('span').text.strip()
    return website1


webpages = []
expiration = []     # X-axis
strike = []         # Z-axis
interest = []       # Y-axis
index_foreach = []  # index value for each table from webpages

url = 'https://finance.yahoo.com/quote/FAS/options?date=1564704000'
r = requests.get(url)
webpages = get_webpages(url)

for page in webpages:
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('.calls tbody tr')
    expiration.append(get_dates(page))

    for row in rows:

        strike_price = row.select_one('.data-col2').text.strip()
        strike_price = float(strike_price)
        strike.append(strike_price)
        open_interest = row.select_one('.data-col9').text.strip()
        open_interest = float(open_interest)
        interest.append(open_interest)

    index_foreach.append(len(strike))
"""
print(len(strike))
print(len(interest))
# print(len(rows))
print(webpages)
print(expiration)
"""
# interest = x axis
# strike = y axis

fig, axes = plt.subplots(nrows=1, ncols=3)

find_index1 = index_foreach[1] - index_foreach[0]
find_index2 = index_foreach[2] - index_foreach[1]

axes[0].scatter(interest[:index_foreach[0]], strike[:index_foreach[0]])
axes[0].set_title(expiration[0])

axes[1].scatter(interest[:find_index1], strike[:find_index1])
axes[1].set_title(expiration[1])

axes[2].scatter(interest[:find_index2], strike[:find_index2])
axes[2].set_title(expiration[2])

plt.tight_layout()
plt.show()
