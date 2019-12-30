#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/12/

from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)
testvalue = bob.role
print(bob.role)


# define exception classes here
class UserDoesNotExist(Exception):
    pass


class UserAccessExpired(Exception):
    pass


class UserNoPermission(Exception):
    pass


def get_secret_token(username):
    print(bob)
    if username in [User.name for User in USERS]:
        username = username.lower()
        print(username)
        if username.expired is True:
            if username.role == ADMIN:
                return SECRET
            else:
                raise UserNoPermission
        else:
            raise UserAccessExpired
    else:
        raise UserDoesNotExist

if __name__ == '__main__':
    print(get_secret_token('PyBites'))
