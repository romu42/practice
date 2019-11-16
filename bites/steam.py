#!/usr/bin/env python3
# by rog
# https://codechalleng.es/bites/55/

from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    games = []
    d = feedparser.parse(FEED_URL)
    for item in d.entries:
      games.append(Game(item['title'], item['link']))
    return games




if __name__ == '__main__':
    get_games()