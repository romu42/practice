#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/172/


from functools import partial


def round_it(number, round_value):
    return round(number, round_value)

rounder_int = partial(round_it, round_value=0)
rounder_detailed = partial(round_it, round_value=4)


