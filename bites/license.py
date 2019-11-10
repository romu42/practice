#!/usr/bin/env python3
# by rog

import secrets
import string


def gen_key(*, parts=4, chars_per_part=8):
    passwordchars = string.ascii_uppercase + string.digits
    return "-".join(
        "".join(secrets.choice(passwordchars) for input in range(chars_per_part))
        for count in range(parts)
    )


if __name__ == "__main__":
    print(gen_key())
