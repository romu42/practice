#!/usr/bin/env python3
# by rog


"""
pythonmorsels.com

For this week's exercise I want you to write a function that accepts a sequence (a list for example) and
returns a new iterable (anything you can loop over) with adjacent duplicate values removed.

For example:

>>> compact([1, 1, 1])
[1]
>>> compact([1, 1, 2, 2, 3, 2])
[1, 2, 3, 2]
>>> compact([])
[]

"""
from itertools import groupby
from operator import itemgetter

# found solution under itertools, good google foo.. :(
def compact(iterable: list) -> iter:
    return map(next, map(itemgetter(1), groupby(iterable)))


# own solution, doesn't fix bonus #1 or bonus #2
# def compact(iterable: list) -> iter:
#     uniq_elements = [0, ]
#     while iterable:
#         next_element = iterable.pop(0)
#         if uniq_elements[-1] != next_element:
#             uniq_elements.append(next_element)
#     uniq_elements.pop(0)
#     return uniq_elements



if __name__ == '__main__':
    print(compact(n**2 for n in [1, 2, 2]))




