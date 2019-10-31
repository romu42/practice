

from datetime import datetime, date, timedelta
from itertools import islice, takewhile

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    pybites_day = PYBITES_BORN + timedelta(days=100)
    pybites_year = PYBITES_BORN + timedelta(days=365)
    while True:
        if pybites_day < pybites_year:
            yield pybites_day
            pybites_day += timedelta(days=100)
        elif pybites_year < pybites_day:
            yield pybites_year
            pybites_year += timedelta(days=365)








if __name__ == '__main__':
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 10))
    for date in dates:
        print(date)