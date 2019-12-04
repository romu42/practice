# https://codechalleng.es/bites/153/

def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    if up:
        return [int(x) + 1 for x in transactions]
    else:
        return [int(x) for x in transactions]
