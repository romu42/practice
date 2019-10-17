#!/usr/bin/env python3
# by rog

import types
from collections import deque


def tail(sequence: iter, number: int) -> iter:
    if number <= 0:
        return []

    elif isinstance(sequence, types.GeneratorType):
        d = deque(sequence)
        if d:
            return [d[x] for x in range(-number, 0)]
        else:
            return []

    else:
        return list(sequence[-number:])



