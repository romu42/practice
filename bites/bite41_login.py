#!/usr/bin/env python3

# https://codechalleng.es/bites/41/ 

import functools

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = args[0]
        if user in loggedin_users:
            message = f'welcome back {user}'
        elif user in known_users:
            #print(f'please login')'
            message = f'please login'
        else:
            #print('please create an account')
            message = 'please create an account'
        return message
    return wrapper





@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    pass

