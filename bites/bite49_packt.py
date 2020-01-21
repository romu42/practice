#!/usr/bin/env python3

# https://codechalleng.es/bites/49/

from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests
import pprint

pp = pprint.PrettyPrinter()


PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'lxml')
    #mydivs = soup.find_all('div', id='deal-of-the-day')
    #print(dir(mydivs))
    #description = mydivs[0].contents[1].text.replace('\t', '')
    #print((description.split('\n')))
    mydivs = soup.find_all('div', class_='dotd-main-book-summary float-left')

    for div in mydivs:
        #print(div)
        print('bobobobobobobobbo')
        print(div.text.strip())
    # works for title
    #title = soup.find('div', class_='dotd-title')
    #print(title.text.strip())
    #img = soup.find_all('div', class_='bookimage imagecache imagecache-dotd_main_image')
    #print(img.text.strip())

if __name__ == '__main__':
    get_book()
