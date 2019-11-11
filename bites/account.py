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
        if isinstance(input, int):
            self._transactions.append(input)
        else:
            raise ValueError


    def __sub__(self, input):
        if isinstance(input, int):
            self._transactions.append(-input)
        else:
            raise ValueError

    def __gt__(self, other):
        if self.balance > other.balance:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.balance >= other.balance:
            return True
        else:
            return False


    def __lt__(self, other):
        if self.balance < other.balance:
            return True
        else:
            return False


    def __le__(self, other):
        if self.balance <= other.balance:
            return True
        else:
            return False


    def __eq__(self, other):
        if self.balance == other.balance:
            return True
        else:
            return False


    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"


    def __getitem__(self, item):
        return self._transactions[item]




