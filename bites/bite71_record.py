#!/usr/bin/env python3
# https://codechalleng.es/bites/71/


class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.score = None

    def __call__(self, score):
        if self.score == None:
            self.score = score
            return self.score
        elif self.score < score:
            self.score = score
            return self.score
        else:
            return self.score

