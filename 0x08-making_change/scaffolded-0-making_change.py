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
    RES = 0
    REARRANGED = False

    def f(coins, total):
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

        nonlocal RES, REARRANGED

        if not REARRANGED:
            # sort the list and reverse it to have max first
            coins2 = list(reversed(sorted(coins)))
            REARRANGED = True
        # print('#######')  # SCAFF
        # print('coins: ', coins, 'coins2: ', coins2,
        # ...'rem: ', rem, 'n: ', n)  # SCAFF

        # at this point, we have a positive total, and non-empty list
        while True:
            if rem >= coins2[0]:
                # print(coins2[0])  # SCAFF
                rem -= coins2[0]
                RES += 1
                use_cases += 1
                continue
            else:
                # rem is less than first element in coins;
                # pop it and check a smaller value, if any
                if rem == 0:
                    # result found
                    # print('RES when rem==0: ', RES)  # SCAFF
                    res = RES
                    return res

                num = coins2.pop(0)
                # print('num: ', num)  # SCAFF
                n = len(coins2)
                # print('n: ', n)  # SCAFF
                # print('rem: ', rem)  # SCAFF
                # print('use cases: ', use_cases)  # SCAFF
                # print('RES: ', RES)  # SCAFF
                # print('coins2:', coins2)  # SCAFF

                if n == 0:
                    # backtrack
                    return -1
                # recurse with a non-empty coins2 (coins)
                # ...and positive rem (total)
                res = f(coins2, rem)
                # print('=======')  # SCAFF
                # print('num: ', num, 'res: ', res,
                # ...'coins2:', coins2)  # SCAFF

                # on return from child stack
                if res != -1:
                    # print('result not equal to -1')  # SCAFF
                    # result established; return it
                    return res
                # else implement backtracking;
                # reduce the number of subtracts of
                # ...the number represented by this stack
                # print('use cases after recursion 1: ', use_cases)  # SCAFF
                while use_cases > 0:
                    # print('in second while loop for use_cases')  # SCAFF
                    use_cases -= 1
                    rem += num
                    RES -= 1
                    res2 = f(coins2, rem)
                    # print('in 2nd while loop--> res2:', res2,
                    # ...'coins2:', coins2, 'UC:', use_cases,
                    # ...'rem:', rem, 'RES:', RES)  # SCAFF
                    if res2 != -1:
                        return res2
                return -1

                # num subtracted zero times, and no result yet; nactrack

        # print('####->', RES)
        return RES

    return f(coins, total)


print(makeChange([1, 2, 25], 37))
print(makeChange([8, 9, 4, 72, 2647], 2740))
