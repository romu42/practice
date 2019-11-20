#!/usr/bin/env python3
# by rog
# https://codechalleng.es/bites/20/

class Account:

    def __init__(self):
        self._transactions = []
        # self._current_balance = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager
    def __enter__(self):
        self.current_balance = [transaction for transaction in self._transactions]
        return self


    def __exit__(self, exc_type, exc_value, exc_traceback):
        if sum(self._transactions) < 0:
            self._transactions = self.current_balance