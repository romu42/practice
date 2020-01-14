#!/usr/bin/env python3

# https://codechalleng.es/bites/33/


def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if type(data) == dict:
        keys = []
        values = []
        for k, v in data.items():
            keys.append(k)
            values.append(v)
        uberlist = [keys, values]
        return uberlist

    elif type(data) == list:
        names = []
        days = []
        points = []
        bitecoins = []
        for nt in data:
            names.append(nt.name)
            days.append(nt.since_days)
            points.append(nt.karma_points)
            bitecoins.append(nt.bitecoin_earned)
        uberlist = [names, days, points, bitecoins]
        return uberlist

