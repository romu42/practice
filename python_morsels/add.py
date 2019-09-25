#!/usr/bin/env python3
# by rog


"""
a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
"""


# def add(*nested_lists):
#     matrix3 = ([[sum(items) for items in zip(*zipped_list)] for zipped_list in zip(*nested_lists)])
#     return matrix3

def add(*nested_lists):
    length = (len(nested_lists[0]))
    if any(len(lst) != length for lst in nested_lists):
        raise ValueError('Given matrices are not the same size.')
    for zipped_list in zip(*nested_lists):
        length = (len(zipped_list[0]))
        if any(len(lst) != length for lst in zipped_list):
            raise ValueError('Given matrices are not the same size.')
    matrix3 = ([[sum(items) for items in zip(*zipped_list)] for zipped_list in zip(*nested_lists)])
    return matrix3

if __name__ == '__main__':
    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    print(add(matrix1, matrix2))


# bonus 1 accept any number of  lists
# exception raise ValueError("Given matrices are not the same size.")