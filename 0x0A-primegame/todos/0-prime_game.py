#!/usr/bin/python3
""" The prime game puzzle.
"""


class Prime:
    """ Class to manage prime numbers and related data.
    """
    primes = {}
    multiple_lengths = {}
    lengths_list = []
    all_multiples = []  # list of lists

    def update():
        pass

    @classmethod
    def isPrime(number):
        pass

# TODO: make a method of Prime
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
    if x == 0 or not isinstance(nums, list) or not nums:
        return None

    prime = Prime()
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        num_rng = list(range(1, num + 1))
        num_rng_mutate = num_rng.copy()

        # parse and save data in Prime object instance
        for n in num_rng:
            # for only prime numbers in the num_rng range
            if isPrime(n):
                prime.primes[n] = []  # init the prime's data
                # get and save multiples of the prime
                max_multiple = num // n
                for multiple in range(2, max_multiple + 1):
                    product = n * multiple
                    try:
                        # get index of existing list object
                        index = prime.all_multiples.index([product])
                    except ValueError:
                        index = None
                    if (product in num_rng) and index is not None:
                        # append existing multiples list obj
                        prime.primes[n].append(prime.all_multiples[index])
                    elif product in num_rng:
                        # create new multiples list object
                        new_multiple = [product]
                        prime.all_multiples.append(new_multiple)
                        prime.primes[n].append(new_multiple)

        # NEXT: process Prime instance to
        # ...prioritize removing primes with most multiples

        # ============OLD CODE BELOW==============
        turn = 'maria'

        for n in num_rng:
            if isPrime(n):
                turn = 'ben' if turn == 'maria' else 'maria'
                num_rng_mutate.remove(n)
                max_multiple = num // n
                for multiple in range(2, max_multiple + 1):
                    product = n * multiple
                    if product in num_rng_mutate:
                        num_rng_mutate.remove(product)
        if turn == 'maria':
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'

    if maria_wins < ben_wins:
        return 'Ben'

    # else a tie
    return None
