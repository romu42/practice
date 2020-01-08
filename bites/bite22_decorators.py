#!/usr/bin/env python3

# https://codechalleng.es/bites/22/

from functools import wraps


def make_html(element):
    def real_decorator(function):
        @wraps(function)
    def wrapped(*args, **kwargs):
       print(f"<{element}>") 
       element(*args, **kwargs)
       print(f"</{element}>")
    return wrapped


    
