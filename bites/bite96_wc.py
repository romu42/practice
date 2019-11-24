#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/96/

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as input:
        data = input.read()
        words = data.split()
        lines = data.splitlines()
        print('bob')
    return f"{len(lines)} {len(words)} {len(data)} {file_}"


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
