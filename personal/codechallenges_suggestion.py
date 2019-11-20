#!/usr/bin/env python3
# by rog

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import credentials
import requests
from urllib.parse import urlparse


user = credentials.user
password = credentials.password
catalogue = set()
C_days_bites = set()

driver = webdriver.Chrome()
driver.get("https://codechalleng.es/login")

assert "PyBites" in driver.title
driver.find_element_by_name('username').send_keys(user)
pw_and_enter = password + Keys.RETURN
driver.find_element_by_name('password').send_keys(pw_and_enter)
driver.get("https://codechalleng.es/")
results = driver.page_source
soup = BeautifulSoup(driver.page_source, 'lxml')
table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="filterList")

for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if '✔' in tds[0].text:
        next
    else:
        url = urlparse(tds[1].contents[1].attrs['href'])
        catalogue.add(url.path)
driver.quit()

result_100days = requests.get('https://codechalleng.es/100days/romu42/4829')
soup = BeautifulSoup(result_100days.content, 'lxml')

for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')
    try:
        url = urlparse(tds[1].contents[1].attrs['href'])
        C_days_bites.add(url.path + '/')
    except:
        pass

listobites = sorted(catalogue.difference(C_days_bites), key=lambda x: int(x.rstrip('/').split('/')[-1]))

print('hey rog try one of these bites\n')
for bite in listobites:
    print(f"https://codechalleng.es{bite}")
