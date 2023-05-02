#!/usr/bin/env python3
import sys

n = int(sys.argv[1])


def getPrimeDivisor(n: int) -> int:
    ''' Return the lowest prime divisor of @n.
    '''
    if n > 0 and n < 4:
        # n between 1 and 3 (inclusive)
        return n

    # n > 3
    divisor: int = 2
    remainder: int = 1  # seed
    limit: int = n // 2

    while remainder != 0:
        remainder = n % divisor
        if remainder != 0:
            divisor += 1
        if divisor > limit:
            # no number can be divided by a value more than half its own
            return n

    # remainder equals 0
    return divisor


print(getPrimeDivisor(n))
