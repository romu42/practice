#!/usr/bin/env python3

# https://codechalleng.es/bites/30/import csv


from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
import csv
from statistics import mean

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    all_movies = {}
    with open(MOVIE_DATA, encoding='utf-8') as f:
        data = csv.reader(f)
        for line in data:
            line = [item.rstrip() for item in line]
            if len(line[23]) < 4 or line[23] == 'title_year':
                continue
            try:
                year = int(line[23])
            except:
               # print(f"director:{line[1]} titel:{line[11]} year:{line[23]} score:{line[25]}")
                continue 
            if year < 1960:
                continue 
            if line[1] in all_movies:
                all_movies[line[1]].append(Movie(line[11],  line[23], line[25]))
            else:
                all_movies[line[1]] = [Movie(line[11],  line[23], line[25])]
            #print(f"director:{line[1]} titel:{line[11]} year:{line[23]} score:{line[25]}")

        #print(all_movies)
        #print(all_movies['Sergio Leone'])
        #for item in all_movies['Sergio Leone']:
        #    print(item[2])
    return all_movies

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(mean([float(item.score) for item in movies]), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    director_avg_score = []
    for item in directors:
        if len(directors[item]) >= MIN_MOVIES:
            mean_score = calc_mean_score(directors[item])
            director_avg_score.append((item, mean_score))
    return(sorted(director_avg_score, key = lambda x: x[1], reverse=True))


       # print(type(directors[item]))


if __name__ == '__main__':
    get_average_scores(get_movies_by_director())
