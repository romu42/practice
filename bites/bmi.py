#!/usr/bin/env python3
# by rog
# https://codechalleng.es/bites/56/

import argparse


def calc_bmi(weight, length):
    """Provided/DONE:
       Calc BMI give a weight in kg and length in cm, return the BMI
       rounded on 2 decimals"""
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


def create_parser():
    """TODO:
       Create an ArgumentParser adding the right arguments to pass the tests,
       returns a argparse.ArgumentParser object"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--WEIGHT", type=int, help="Your weight in kg", dest="weight")
    parser.add_argument("-l", "--LENGTH", type=int, help="Your length in cm", dest="length")
    return parser

def handle_args(args=None):
    """Provided/DONE:
       Call calc_bmi with provided args object.
       If args are not provided get them from create_parser"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f'Your BMI is: {bmi}')
    else:
        # could enforce SystemExit in create_parser/add_argument, but argparse
        # docs are not clear how to do it, so raising the exception here manually
        raise SystemExit


if __name__ == '__main__':
    handle_args()