#!/usr/bin/env python3
# by rog


def tail(sequence: iter, number: int) -> iter:
    print(type(sequence))
    if sequence is list:
        return(sequence[-number:])
    else:
        return False