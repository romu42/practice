#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/91/

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    for char in input_str.lower():
        if char in VOWELS:
            continue
        else:
            return False
    return True



def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    for char in input_str.lower():
        if char in PYTHON:
            return True
        else:
            continue
    return False


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    for char in input_str:
        if char.isdigit():
            return True
        else:
            continue
    return False
