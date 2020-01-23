#!/usr/bin/env python3

# https://codechalleng.es/bites/49/

from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests
import pprint
import re

pp = pprint.PrettyPrinter()


PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'lxml')
    divs = soup.find('div', class_='dotd-title')
    title = (divs.text.strip())
    next = divs.next_sibling
    next = next.next_sibling
    next = next.next_sibling
    description = (next.next_sibling.text.strip())
    divs = soup.find('div', class_='dotd-main-book-image float-left')
    image = ((divs.contents[1].contents[1].contents[0].attrs['src']))
    link = ((divs.contents[1].attrs['href']))
    return Book(title, description, image, link)

if __name__ == '__main__':
    get_book()
