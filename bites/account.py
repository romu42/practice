#!/usr/bin/env python3
# by rog

class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below

    def __len__(self):
        return len(self._transactions)

    def __add__(self, input):
        self._transactions.append(input)

    def __sub__(self, input):
        self._transactions.append(-input)

