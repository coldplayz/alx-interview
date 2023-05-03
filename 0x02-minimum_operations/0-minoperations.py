#!/usr/bin/python3
''' Optimize operations.'''


def getPrimeDivisor(n: int) -> int:
    ''' Return the lowest prime divisor of @n.
    '''
    if n > 0 and n < 4:
        # n between 1 and 3 (inclusive)
        return n

    # n > 3
    divisor = 2
    remainder = 1  # seed
    limit = n // 2

    while remainder != 0:
        remainder = n % divisor
        if remainder != 0:
            divisor += 1
        if divisor > limit:
            # no number can be divided by a value more than half its own...
            return n  # ...except that value is itself

    # remainder equals 0
    return divisor


def minOperations(n: int) -> int:
    ''' Calculates the fewest number of operations needed to
    result in exactly n H characters in a file.

    In a text file, there is a single character H. Your text editor can
    ...execute only two operations in this file: Copy All and Paste.

    Process:
        Given a target number of characters, 18, and
        ...starting with one character. I figured the fastest way to
        ...get to 18 was to copy 9 characters (18 / 2) and paste them
        ...once (a total of 2 operations). But then, how do you get to
        ...9 characters, fastest? 9 is not divisible by 2 but 3 is.
        So the fastest way to get to 9 characters is to
        ...copy 3 characters (9 / 3) and paste them two
        ...times (a total of 3 operations).
        Next, how do you get to three characters? 3 is
        ...not divisible by 2, but 3 is. So the fastest way to
        ...get to 3 characters is to copy 1 character (3 / 3) and
        paste them two times (a total of 3 operations).

        This produced a pattern that led to my implementation,
        ...using recursion. A key part of this observed pattern is that
        ...the divisor of the target number equals the number of operations to
        ...be performed to achieve the end goal of reaching the
        ...target number at each stage of the breakdown (18 to 9 to 3).

        I needed to figure out the number of characters to copy and paste,
        ...in the minimum amount of times to reach a target number.
        The solution was to divide the target number by
        ...its smallest prime factor. The quotient is guaranteed to be
        ...greater than or equal to the divisor, and if you add
        ...this quotient the number of times of the divisor,
        ...you arrive at the target number in the fewest additions.

        I implemented a helper function to produce the
        ...magic prime number. And once I figured out the
        ...base case and flow of the recursion, I was all set.
    '''
    if n < 2:
        # This targets the first/initial value of n
        return 0

    minPrimeDivisor = getPrimeDivisor(n)
    quotient = n // minPrimeDivisor

    if quotient == 1:
        # Base case
        return minPrimeDivisor

    return minPrimeDivisor + minOperations(quotient)
