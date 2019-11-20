#!/usr/bin/env python3
# by rog
# https://codechalleng.es/bites/68/


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return input_string.translate({ord(i): None for i in ')(!.-|,:^?;\''})
