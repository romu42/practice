#  https://codechalleng.es/bites/189/

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5
DIGITS = ''


def filter_names(names):
    send_back = []
    for item in names:
        if item[0] == IGNORE_CHAR:
            continue
        elif any(char.isdigit() for char in item):
            continue
        elif item[0] == QUIT_CHAR:
            return send_back
        elif len(send_back) == MAX_NAMES:
            return send_back
        else:
            send_back.append(item)
    return send_back
