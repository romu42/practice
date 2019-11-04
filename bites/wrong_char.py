#!/usr/bin/env python3
# by rog

def get_index_different_char(chars):
    charcount = 0
    charcount_index = 0
    noncharcount = 0
    noncharcount_index = 0

    for count, char in enumerate(chars):
        char = str(char)
        if char.isalnum():
            charcount += 1
            charcount_index = count
        else:
            noncharcount += 1
            noncharcount_index = count

    if charcount == 1:
        return charcount_index
    else:
        return noncharcount_index
