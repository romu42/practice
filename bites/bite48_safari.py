#!/usr/bin/env python3

# https://codechalleng.es/bites/48/

import os
import urllib.request
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    graph_data = defaultdict(list)
    with open(SAFARI_LOGS) as file:
        data = file.read()
    entries = data.split('\n')
    for line_nr, entry in enumerate(entries):
        if 'sending to slack channel' in entry:
            book = entries[line_nr - 1].split(' ')
            if 'Python' in book:
                graph_data[book[0]].append(PY_BOOK)
            else:
                graph_data[book[0]].append(OTHER_BOOK)
    for k in graph_data:
        print(k, ''.join(graph_data[k]))


if __name__ == '__main__':
    create_chart()
