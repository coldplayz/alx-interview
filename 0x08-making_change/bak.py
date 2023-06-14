#!/usr/bin/python3
""" Algorithm practice: making change.
"""


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
    res = 0
    n = len(coins2)

    if n == 0:
        # empty coins list; constraint 2
        return -1

    # sort the list and reverse it to have max first
    coins2 = list(reversed(sorted(coins)))
    # print(coins, coins2)

    # at this point, we have a positive total, and non-empty list
    while n and rem > 0:
        if rem >= coins2[0]:
            print(coins2[0])
            rem -= coins2[0]
            res += 1
        else:
            # rem is less than first element in coins;
            # pop it and check a smaller value, if any
            coins2.pop(0)

        n = len(coins2)

    if res == 0 or (n == 0 and rem != 0):
        print('####->', f'res: {res}, n: {n}, rem: {rem}')
        # constraint 2
        # total is not greater than any element in coins...
        # ...OR non of the values in coins can
        # sum up to exactly total, in any combination
        return -1

    print('####->', res)
    # return res


# makeChange([1, 2, 25], 37)
makeChange([8, 9, 4, 72, 2647], 2740)
