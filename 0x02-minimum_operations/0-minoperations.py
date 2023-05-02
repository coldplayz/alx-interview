#!/usr/bin/python3
''' Optimize operations.'''


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


def minOperations(n: int) -> int:
    ''' Calculates the fewest number of operations needed to
    result in exactly n H characters in a file.

    In a text file, there is a single character H. Your text editor can
    ...execute only two operations in this file: Copy All and Paste.

    Implemented using recursion.
    '''
    if n < 2:
        # This targets the first/initial value of n
        return 0

    minPrimeDivisor: int = getPrimeDivisor(n)
    quotient: int = n // minPrimeDivisor

    if quotient == 1:
        # Base case
        return minPrimeDivisor

    return minPrimeDivisor + minOperations(quotient)
