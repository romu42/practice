#!/usr/bin/env python3
# by rog
# https://codechalleng.es/bites/54/

import textwrap

INDENTS = 4


def print_hanging_indents(poem):
    indent = False
    dedented_text = textwrap.dedent(poem).strip()
    for line in dedented_text.splitlines():
        if indent is False:
            print(f"{line}")
            indent = True
        elif not line.strip():
            indent = False
        else:
            print(f"    {line}")



if __name__ == '__main__':
    print_hanging_indents("""
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """)