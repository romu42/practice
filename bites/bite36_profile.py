#!/usr/bin/env python3

# https://codechalleng.es/bites/36/

def get_profile(name, age, *args, **kwargs):
    profile = {}
    if type(age) != int:
        raise ValueError
    if len(args) > 5 :
        raise ValueError
    profile['name'] = name
    profile['age'] = age
    if args:
        profile['sports'] = sorted(args)
    if kwargs:
        profile['awards'] = kwargs
    return profile
