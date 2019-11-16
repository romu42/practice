#!/usr/bin/env python3
# by rog
# https://codechalleng.es/bites/66/

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    total = 0
    averages = []
    for number in enumerate(sequence, start=1):
        total += number[1]
        averages.append(round(total/number[0], 2))
    return averages


