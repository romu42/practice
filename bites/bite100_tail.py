#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/100/

def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath, 'r') as input:
        lines = input.read().splitlines()
        return(lines[-n:])
