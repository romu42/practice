#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/77/

def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    return len(set(my_cities).symmetric_difference(other_cities))