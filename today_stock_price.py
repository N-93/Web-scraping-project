# -*- coding: utf-8 -*-
"""Today Stock Price

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pT4s2bgJRkGX6LwEJoMicyLWx0BrZyKF
"""

import os
import requests

url = 'https://www.sharesansar.com/today-share-price'

print(url)

response = requests.get(url)
print(response)
#print(response.content)

print(response.content)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.content, 'html.parser')
##print(soup.prettify()[:500])

#world_data = soup.find("tbody").find_all('tr')
#print(world_data)

stock_data = soup.find("tbody").find_all('tr')
##print(stock_data)

for data in stock_data:
    print(data)
    break

print(stock_data)

print(len(stock_data))

complete_data = []
for i in range(0, len(stock_data)):
  data = []
  list_data = stock_data[i].find_all("td")
  for i in list_data:
    data.append(i.text)
    complete_data.append(data)
  # world_data[7].find_all('td')



print(data)

#mapped_data = list(map(lambda x: x[1:10] + [x[12]] + [x[14]], complete_data))

mapped_data = list(map(lambda x : x[1:],complete_data))

print(mapped_data)

column_names = [
    "Symbol",
    "Stock Confidance",
    "Open",
    "High",
    "Low",
    "Close",
    "VWAP",
    "Volume",
    "Previous Closing",
    "Turnover",
    "Trans",
    "Diff",
    "Range",
    "Diff%",
    "Range%",
    "VWAP",
    "120 Days",
    "180 Days",
    "52 Weeks High",
    "52 Weeks Low"

    ]

import pandas as pd

df = pd.DataFrame(mapped_data, columns = column_names)
print(df)
df.to_csv('today_share_price.csv', index=False)

df = pd.read_csv('today_share_price.csv')
df.head()

df.isnull().sum()

# plot the missing data
df.isnull()

missing_data = df.isnull().sum()
missing_data

import seaborn as sns
import matplotlib.pyplot as plt # import pyplot module from matplotlib, pyplot module is a sub-module within `matplotlib`

sns.heatmap(df.isnull().T)

df.head()