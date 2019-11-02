#!/usr/bin/env python3
# by rog

import requests
from bs4 import BeautifulSoup

# result = requests.get('https://codechalleng.es/100days/4829')
result = requests.get('https://codechalleng.es/bites/')


# print(result.status_code)
# print(result.headers)


src = result.content
# print(src)

# soup = BeautifulSoup(src, features="html.parser")
soup = BeautifulSoup(src, 'lxml')
links = soup.find_all("a")

# print(links)
# # print("\n")
#
for link in links:
    # print(link)
    if "/bites/" in link:
        print(link.attrs['href'])