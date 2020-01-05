# https://codechalleng.es/bites/14/

import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*data):
    string_lists = [tuple(str(elem) for elem in sub) for sub in list(zip(*data))]
    print(string_lists)
    final_list = []
    for item in  string_lists:
        print(SEPARATOR.join((item)))
        final_list.append(SEPARATOR.join((item)))
    return final_list

