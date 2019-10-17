#!/usr/bin/env python3
# by rog


def sum_numbers(numbers=None):
    if numbers == []:
        return 0
    elif numbers:
        return sum(x for x in numbers)
    else:
        return sum(x for x in range(1, 101))

