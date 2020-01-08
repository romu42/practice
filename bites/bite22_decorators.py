#!/usr/bin/env python3

# https://codechalleng.es/bites/22/

from functools import wraps


def make_html(element):
    def middle(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{element}>{result}</{element}>"
        return wrapper
    return middle



    
