from mpl_toolkits.mplot3d import axes3d
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
    expired = []
    website = soup.select_one('.qsp-2col-options div span')
    website1 = website.find_next_sibling('span').find_next_sibling('span').text.strip()
    expired.append(website1)
    return expired
"""
def get_webpages(url):
#    r = soup.select('.Fz\(s\) option=["value"]')
#    r = soup.select_one(".Fz\((s\))")
#    r = soup.select('.drop-down-selector select')
#    dates = soup.select('div select')
#    r = soup.find_all('select', attrs={'class': 'Fz(s)'})
#    for tag in r.select('option'):
    print(r)
"""

webpages = []
expiration = []
url = 'https://finance.yahoo.com/quote/FAS/options?date=1564704000'
r = requests.get(url)
webpages = get_webpages(url)
print(webpages)


soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('.calls tbody tr')

expiration = get_dates(url)
print(expiration)
#test = soup.select_one('.qsp-2col-options div span')
#next = test.find_next_sibling('span').find_next_sibling('span').text.strip()
#print(next)


strike = []
interest = []

for page in pages:
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('.calls tbody tr')
"""
for row in rows:

    strike_price = row.select_one('.data-col2').text.strip()
    strike_price = float(strike_price)
    strike.append(strike_price)
    open_interest = row.select_one('.data-col9').text.strip()
    open_interest = float(open_interest)
    interest.append(open_interest)
"""
print(strike[0])
print(interest[0])
print(len(rows))
"""

fig = plt.figure(figsize = (9, 6))
graph = fig.add_axes([0.1, 0.1, 0.9, 0.9])
graph.scatter(interest, strike)
graph.set_xlabel('interest')
graph.set_ylabel('strike')
#plt.show()
