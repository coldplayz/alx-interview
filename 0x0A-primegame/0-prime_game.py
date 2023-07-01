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
    # print(n)  # SCAFF

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
    # results = {}  # {prime: number of multiples, incl 1}
    max_num = max(nums)
    multiples = []  # all multiples across rounds
    # current_primes = []  # all prime numbers across rounds

    for n in range(1, max_num + 1):
        # record all multiples/composites for all primes
        # ...not greater than the square root of max_num
        if n in multiples:
            # n is not prime
            continue

        if (n ** 2) > max_num:
            break

        if isPrime(n):
            # multiples.append(n)
            # record its multiples as non-prime
            max_multiple = max_num // n
            for i in range(2, max_multiple + 1):
                multiple = n * i
                if multiple not in multiples:
                    multiples.append(multiple)
            # remove duplicates
            # multiples = list(set(multiples))

    # process the collected data
    for num in nums:
        # get multiples for a specific round
        num_multiples = list(filter(lambda x: x <= num, multiples))
        # total multiples plus one for 1 (a non-prime)
        multiples_len = len(num_multiples) + 1
        # determine round winner
        num_primes = num - multiples_len

        if num_primes % 2 == 0:
            # Ben wins for even number of primes as Maria starts always
            # print('round winner: Ben')  # SCAFF
            ben_wins += 1
        else:
            # Maria wins for odd number of primes
            # print('round winner: Maria')  # SCAFF
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'

    if maria_wins < ben_wins:
        return 'Ben'

    # else a tie
    return None