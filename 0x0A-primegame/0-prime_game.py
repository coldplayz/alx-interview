#!/usr/bin/python3
""" The prime game puzzle.
"""


def isPrime(n):
    """ Determine if the number, n, is a prime number.
    """
    if type(n) is not int or n < 2:
        return False

    limit = n // 2
    divisors = 0

    for divisor in range(1, limit + 1):
        if (n % divisor) == 0:
            divisors += 1

        if divisors > 1:
            return False

    if divisors > 1:
        return False
    return True


def isWinner(x, nums):
    """ Solves the prime game puzzle.
    """
    if x < 1 or not isinstance(nums, list) or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        num_rng = list(range(1, num + 1))
        num_primes = 0

        for n in num_rng:
            if isPrime(n):
                num_primes += 1

        if num_primes % 2 == 0:
            # Ben wins for even number of primes as Maria starts always
            ben_wins += 1
        else:
            # Maria wins for odd number of primes
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'

    if maria_wins < ben_wins:
        return 'Ben'

    # else a tie
    return None
