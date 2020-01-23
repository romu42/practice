#!/usr/bin/env python3

# https://codechalleng.es/bites/51/

from datetime import datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""

    td = (PY2_DEATH_DT - start_date)
    return round((td.days*24 + td.seconds/3600), 1)


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)
       1 hour to 7 earth years
       """

    td = (PY2_DEATH_DT - start_date)
    return round(((td.days*24 + td.seconds/3600)/1022), 2)
