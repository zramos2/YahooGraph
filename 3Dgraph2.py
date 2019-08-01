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

"""
print(len(strike))
print(len(interest))
# print(len(rows))
print(webpages)
print(expiration)
"""

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(expiration, interest, strike, marker='o')
ax.set_xlabel('Expiration Date')
ax.set_ylabel('Open Interest')
ax.set_zlabel('Strike Price')
plt.show()

"""
graph = fig.add_axes([0.1, 0.1, 0.9, 0.9])
graph.scatter(interest, strike)
graph.set_xlabel('Open Interest')
graph.set_ylabel('Strike Price')
plt.show()

"""
