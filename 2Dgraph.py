import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

"""
url = 'https://www.allsides.com/media-bias/media-bias-ratings'
r = requests.get(url)
#print(r.content[:100])

soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')

row = rows[0]
name = row.select_one('.source-title').text.strip()
print(name)
"""
url = 'https://finance.yahoo.com/quote/FAS/options?date=1564704000'
r = requests.get(url)
#print(r.content[:100])

soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')
row = rows[0]

strike = row.select_one('.data-col2').text.strip()
print(strike)

open_interest = row.select_one('.data-col9').text.strip()
print(open_interest)
