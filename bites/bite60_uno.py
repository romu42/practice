#!/usr/bin/env python3
# https://codechalleng.es/bites/60/

from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')
names2 = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'Skip',
    'Reverse',
    'Draw Two',
    ]
wilds = ['Wild', 'Wild Draw Four']

def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    cards = []
    for suit in SUITS:
        cards.append(UnoCard(suit, '0'))
        for name2 in names2:
            cards.append(UnoCard(suit, name2))
            cards.append(UnoCard(suit, name2))
    for wild in wilds:
        cards.append(UnoCard(None, wild))
        cards.append(UnoCard(None, wild))
        cards.append(UnoCard(None, wild))
        cards.append(UnoCard(None, wild))
    return cards

if __name__ == '__main__':
    create_uno_deck()
