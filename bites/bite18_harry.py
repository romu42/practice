#!/usr/bin/env python3

# https://codechalleng.es/bites/18/

import os
import urllib.request
import string
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)
printable = set(string.printable)
punctuation = set(string.punctuation)

def get_harry_most_common_word():
    with open(stopwords_file) as file:
        stopwords_list = [item.rstrip() for item in file]
    with open(harry_text, 'r+', encoding='utf-8') as file:
        data = file.read()
        data = data.translate(str.maketrans('', '', string.punctuation))
        data = data.replace('\n', ' ')
        data = ''.join(filter(lambda x: x in printable, data))
        data = [x.lower() for x in data.split(' ') if x.lower() not in stopwords_list]
        data = [x for x in data if len(x) > 1]
        return Counter(data).most_common(1)[0]

if __name__ == '__main__':
    get_harry_most_common_word()
