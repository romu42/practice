#!/usr/bin/env python3
# https://codechalleng.es/bites/60/

from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name', defaults=None)


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    cards = []
    for suit in SUITS:
        UnoCard = 


if __name__ == '__main__':
    create_uno_deck()
