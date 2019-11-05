#!/usr/bin/env python3
# by rog

import requests
import urllib3
from bs4 import BeautifulSoup

# result = requests.get('https://codechalleng.es/100days/4829')
result = requests.get('https://codechalleng.es/bites/')


# print(result.status_code)
# print(result.headers)


src = result.content
# print(src)

# soup = BeautifulSoup(src, features="html.parser")
soup = BeautifulSoup(src, 'lxml')

for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')
    print(tds[0].contents[1].attrs['href'])