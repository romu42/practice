#!/usr/bin/env python3

# https://codechalleng.es/bites/27/

import json
import re
import operator

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movie_list = []
    for file in files:
        with open(file) as f:
            data = f.read()
            movie_dict = json.loads(data)
            movie_list.append(movie_dict)
    return movie_list

def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']

def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    movie_nominations = {}
    for movie in movies:
        m = re.search(r'(\d+)\snominations', movie['Awards'])
        movie_nominations[movie['Title']] = int(m.group(1))
    return max(movie_nominations, key=lambda key: movie_nominations[key])


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    movie_runtimes = {}
    for movie in movies:
        m = re.search(r'(\d+)\smin', movie['Runtime'])
        movie_runtimes[movie['Title']] = int(m.group(1))
    return max(movie_runtimes, key=lambda key: movie_runtimes[key])

