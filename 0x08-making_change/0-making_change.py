#!/usr/bin/python3
""" Algorithm practice: making change.
"""

# implement memoization of results
MEMORY = {}


# IMPROVE: to also provide use case data from
# ...the divisors queue instead of just from the multiplier
def giveUpUseCases(
        multiples: int,
        multiplier: int,
        divisors: list,
        constant: int) -> int:
    """ Determines if divisor can divide into sum of a multiple and constant.

    The multiple is progressively derived from the range:
        1 * multiplier...multiples * multiplier

    If multiples is 0, or divisor is found to never divide
    ...into any multiple, return -1, else return the quotient.
    """
    if multiples == 0 or len(divisors) == 0:
        return -1

    use_cases = 0
    stack_len = 0
    res_list = []

    def f(mps: int, mpr: int, div: list, con: int) -> int:
        """ Enables recursion and a closure for giveUpUseCases.

        Implements going through a divisors queue to find a solution.
        """
        nonlocal use_cases, stack_len

        if len(div) == 0:
            # recursion base case
            return -1

        multiple = con
        stack_len += 1
        stack_num = stack_len

        for i in range(mps):
            multiple += mpr
            # quot = multiple // div[0]
            rem = multiple % div[0]

            if stack_num == 1:
                # in 1st f call where we are tracking multiplier use cases
                use_cases = i + 1

            if rem == 0:
                # return use cases for the original multiplier to give up
                return use_cases

            # there is a remainder; recurse for next divisor
            res = f(1, rem, div[1:], 0)

            if res != -1:
                # return use cases
                return res

        return -1

    for i in range(len(divisors)):
        # get results with all divisors being first element in turn;
        # ...this eliminates false/premature negative result
        res = f(multiples, multiplier, divisors[i:], constant)
        # reset use cases and stack length variables
        use_cases = 0
        stack_len = 0
        res_list.append(res)

    # print(res_list)  # SCAFF

    # filter -1 out and get minimum use_cases
    filtered_res_list = list(filter(lambda x: x != -1, res_list))
    if not filtered_res_list:
        # empty list
        return -1
    min_useCase = min(filtered_res_list)

    return min_useCase


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to meet a given total.

    Args:
        - coins (list): a list of the values of the coins in possession.
        - total (int): the sum to be met by values in coins.

    Returns:
        - int: the fewest number of coins needed to meet total.

    Constraints:
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have, return -1

    Assumptions:
        - You can assume you have an
          infinite number of each denomination of coin in the list.
        - The value of a coin will always be an integer greater than 0.
    """
    global MEMORY

    # see if this use case has been solved already
    # IMPROVE: sorting coins first
    strTotal = str(total)
    strCoins = str(coins)
    case = strTotal + strCoins
    result = MEMORY.get(case, None)
    if result:
        return result

    RES = 0
    REARRANGED = False
    # f_callCount = 0  # SCAFF

    def f(coins, total):
        nonlocal RES, REARRANGED
        # nonlocal f_callCount

        """
        # start SCAFF
        f_callCount += 1
        print('############################')
        print(f'\nf_callCount: {f_callCount};;rem: {total};;RES: {RES}\n')
        # end SCAFF
        """

        if total <= 0:
            # constraint 1
            return 0

        coins2 = coins.copy()
        rem = total
        use_cases = 0  # number of times num is subtracted in this stack
        n = len(coins2)

        if n == 0:
            # empty coins list; constraint 2
            return -1

        if not REARRANGED:
            # ensure coins list is unique
            coins2 = list(set(coins))
            # sort the list and reverse it to have max first
            coins2 = list(reversed(sorted(coins2)))
            REARRANGED = True

        # at this point, we have a positive total, and non-empty list
        while True:
            if rem >= coins2[0]:
                # speed up extraction of use_cases to this,
                # ...instead of, multiple iterations, with division
                use_cases = rem // coins2[0]
                rem = rem % coins2[0]
                RES += use_cases
                continue
            else:
                # rem is less than first element in coins;
                if rem == 0:
                    # result found; end recursion
                    res = RES
                    return res

                # pop first element and check a smaller value, if any
                num = coins2.pop(0)
                n = len(coins2)

                if n == 0:
                    # last element of coins2, and no result yet; backtrack
                    return -1
                # recurse with a non-empty coins2 (coins)
                # ...and positive rem (total)
                res = f(coins2, rem)

                # on return from child stack
                if res != -1:
                    # result established; return it
                    return res
                # else implement backtracking;
                # reduce the number of subtracts of
                # ...the number represented by this stack
                # First, determine the number of use cases to give up
                sub_useCases = giveUpUseCases(use_cases, num, coins2, rem)
                if sub_useCases != -1:
                    # guranteed to get a result here
                    use_cases -= sub_useCases
                    rem += num * sub_useCases
                    RES -= sub_useCases
                    res2 = f(coins2, rem)
                    return res2
                # no use cases to give up to produce a result
                return -1

        return RES

    # memoize result
    result = f(coins, total)
    MEMORY[case] = result

    return result


# print(makeChange([1, 2, 25], 37))
# print(makeChange([8, 9, 4, 72, 2647], 2740))
# print(makeChange([4, 971, 5, 81, 1], 108492932))
