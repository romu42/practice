#!/usr/bin/env python

#https://codechalleng.es/bites/47/

import string
import re

PUNCTUATION_CHARS = list(string.punctuation)
used_passwords = set('PassWord@1 PyBit$s9'.split())


# is between 6 and 12 chars long (both inclusive)
def check_length(password):
    if len(password) < 6:
        return False
    elif len(password) > 12:
        return False
    else:
        return True


# has at least 1 digit [0-9]
def check_digits(password):
    if not bool(re.search(r'\d', password)):
        return False
    else:
        return True


# has at least two lowercase chars [a-z]
def check_lowercase(password):
    lowercase = re.search(r'[a-z][a-z]+', password)
    if lowercase == None:
        return False
    elif len(lowercase.group(0)) < 2:
        return False
    else:
        return True


# has at least one uppercase char [A-Z]
def check_uppercase(password):
    uppercase = re.search(r'[A-Z]+', password)
    if uppercase == None:
        return False
    if len(uppercase.group(0)) < 1:
        return False
    else:
        return True


# has at least one punctuation char (use: PUNCTUATION_CHARS)
def check_punctuation(password):
    punct = set(PUNCTUATION_CHARS)
    password = set(password)
    if len(password.intersection(punct)) > 0:
           return True
    else:
           return False


# Has not been used before (use: used_passwords)
def check_is_new(password):
    if password in used_passwords:
        return False
    else:
        used_passwords.add(password)
        return True

def validate_password(password):
    password_status = []
    password_status.append(check_length(password))
    password_status.append(check_digits(password))
    password_status.append(check_lowercase(password))
    password_status.append(check_uppercase(password))
    password_status.append(check_punctuation(password))
    password_status.append(check_is_new(password))
    if False in password_status:
        return False
    else:
        return True
