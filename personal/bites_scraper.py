#!/usr/bin/env python3
# by rog

import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

result_100days = requests.get('https://codechalleng.es/100days/romu42/4829')
result_catalogue = requests.get('https://codechalleng.es/bites/catalogue')

C_days_bites = set()
catalogue = set()

soup = BeautifulSoup(result_100days.content, 'lxml')

for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')
    try:
        url = urlparse(tds[1].contents[1].attrs['href'])
        C_days_bites.add(url.path + '/')
    except:
        pass

soup = BeautifulSoup(result_catalogue.content, 'lxml')
for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')
    url = urlparse(tds[0].contents[0].attrs['href'])
    catalogue.add(url.path)


listobites = list(sorted(catalogue.difference(C_days_bites)))

print('hey rog try one of these bites\n')
for bite in listobites:
    print(f"https://codechalleng.es{bite}")



