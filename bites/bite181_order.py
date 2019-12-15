# https://codechalleng.es/bites/181/

import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        bisect.insort_left(self._numbers, num, lo=0, hi=len(self._numbers))

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)