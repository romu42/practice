#!/usr/bin/env python3
# by rog

from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name: str, expires: datetime):
        self.name = name
        self.expires = expires


    @property
    def expired(self):
        if self.expires < NOW:
            return True
        else:
            return False






""" Write a simple Promo class. Its constructor receives a name str and expires datetime.

Add a property called expired which returns a boolean value indicating whether the promo has expired or not.

Checkout the tests and datetime module for more info. Have fun!"""