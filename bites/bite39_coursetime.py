#!/usr/bin/env python3

# https://codechalleng.es/bites/39/


from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as file:
        times = []
        data = file.read()
        for line in data.split('\n'):
            time = re.search(r'(\d+:\d+)', line)
            if time:
                times.append(time.group(1))
        return times

def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total_time = timedelta()
    for time in timestamps:
        (m, s) = time.split(':')
        d = timedelta(hours=0, minutes=int(m), seconds=int(s))
        total_time += d
    return str(total_time)

