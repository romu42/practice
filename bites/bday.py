#!/usr/bin/env python3
# by rog
# https://codechalleng.es/bites/74/

import calendar
from datetime import date

def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    # my solution
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    return weekdays[calendar.weekday(date.year, date.month, date.day)]

    # their solution
    # weekday = date.weekday()
    # return calendar.day_name[weekday]