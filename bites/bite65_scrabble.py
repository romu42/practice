#!/usr/bin/env python3
# https://codechalleng.es/bites/65/

import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])
    for item in dictionary:
        print(item)


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    listan = []
    words = _get_permutations_draw(draw)
    print(len(words))
    for word in words:
        if word.lower() in dictionary:
            listan.append(word.lower())
    return(listan)

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    maybes = set()
    for i in  range(len(draw)):
        for x in itertools.permutations(draw, i):
            maybes.add("".join(x))
    return maybes



