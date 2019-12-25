# https://codechalleng.es/bites/225/

PYBITES = "pybitesPYBITES"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    newstring = ''
    for char in text:
        if char in PYBITES:
            if char.islower():
                newstring += char.upper()
            elif char.isupper():
                newstring += char.lower()
        else:
            newstring += char
    return newstring

