# https://codechalleng.es/bites/215/

import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """

    return_value = True
    key_list = key.split('-')
    if len(key_list) != 5:
        return_value = False
    elif key_list[0] != 'PB':
        return_value = False
    for key_part in key_list[1:]:
        if len(key_part) != 8:
            return_value = False
        else:
            for x in key_part:
                if x.isupper() == False and x.isdigit() == False:
                    return_value = False

    return return_value


