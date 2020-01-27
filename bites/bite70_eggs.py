#!/usr/bin/env
# https://codechalleng.es/bites/70/

from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit):
        self.limit = limit
        self.x = 0


    def __iter__(self):
        return self


    def __next__(self):
        x = self.x
        if x == self.limit:
            raise StopIteration
        self.x = x + 1
        return f"{choice(COLORS)} egg"
