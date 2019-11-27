#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/115/
import re

def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    count = 0
    for i in text:
        if i == ' ':
            count += 1
        else:
            return count


if __name__ == '__main__':
    print(count_indents('    string'))
