#!/usr/bin/python3
""" Algorithm practice: making change.
"""
RES = 0
REARRANGED = False


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
    if total <= 0:
        # constraint 1
        return 0

    coins2 = coins
    rem = total
    use_cases = 0  # number of times num is subtracted in this stack
    n = len(coins2)

    if n == 0:
        # empty coins list; constraint 2
        return -1

    global RES, REARRANGED

    if not REARRANGED:
        # sort the list and reverse it to have max first
        coins2 = list(reversed(sorted(coins)))
        REARRANGED = True
    # print(coins, coins2)

    # at this point, we have a positive total, and non-empty list
    while True:
        if rem >= coins2[0]:
            # print(coins2[0])
            rem -= coins2[0]
            RES += 1
            use_cases += 1
        else:
            # rem is less than first element in coins;
            # pop it and check a smaller value, if any
            if rem == 0:
                # result found
                res = RES
                RES = 0
                REARRANGED = False
                return res

            num = coins2.pop(0)
            n = len(coins2)

            if n == 0:
                # backtrack
                return -1
            # recurse with a non-empty coins2 (coins) and positive rem (total)
            res = makeChange(coins2, rem)

            # on return from child stack
            if res != -1:
                # result established; return it
                RES = 0
                REARRANGED = False
                return res
            # else implement backtracking;
            # reduce the number of subtracts of
            # ...the number represented by this stack
            while use_cases > 0:
                use_cases -= 1
                rem += num
                RES -= 1
                res2 = makeChange(coins2, rem)
                if res2 != -1:
                    RES = 0
                    REARRANGED = False
                    return res2

            # num subtracted zero times, and no result yet; nactrack
            # print(RES)
            res = -1
            break

    # print('####->', RES)
    RES = 0
    REARRANGED = False
    return res


# print(makeChange([1, 2, 25], 37))
print(makeChange([8, 9, 4, 72, 2647], 2740))
