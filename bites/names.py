#!/usr/bin/env python3
# by rog
# bite 5
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    my_names = set(names)
    return [name.title() for name in my_names]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    split_names = [name.split(' ') for name in names]
    return [" ".join(x) for x in (sorted(split_names, key = lambda x: x[1], reverse=True))]


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    split_names = [name.split(' ') for name in names]
    first_name = [first for first, last in split_names]
    shortest = first_name[0]
    for name in first_name:
        if len(name) < len(shortest):
            shortest = name

    return shortest





if __name__ == '__main__':
    print(dedup_and_title_case_names(NAMES))
    print(sort_by_surname_desc(NAMES))
    print(shortest_first_name(NAMES))

