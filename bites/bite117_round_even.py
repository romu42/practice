#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/117/
import math

def round_even(number):
    """Takes a number and returns it rounded even"""
    frac, whole = math.modf(number)
    if frac == 0.5:
        if int(number + 0.5) % 2 == 0:
            return int(number + 0.5)
        elif int(number - 0.5) % 2 == 0:
            return int(number - 0.5)
    elif frac > 0.5:
        return int(whole) + 1
    else:
        return int(whole)


if __name__ == '__main__':
    print(round_even(1.4))
