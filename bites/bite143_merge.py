# https://codechalleng.es/bites/143/

NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    if type(name) == str:
        name = name.lower()
    if name in group3:
        return group3[name]
    elif name in group2:
        return group2[name]
    elif name in group1:
        return group1[name]
    else:
        return NOT_FOUND