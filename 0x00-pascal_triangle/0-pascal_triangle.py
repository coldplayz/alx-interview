#!/usr/bin/env python3
''' Code Pascal's Triangle.
'''


def pascal_triangle(n):
    ''' Returns a of lists of integers representing the Pascal's triangle of n
    '''
    res = []

    if n <= 0:
        return res
    if n == 1:
        return [[1],]
    if n == 2:
        return [[1], [1, 1]]

    # n is greater than 2
    res.extend([[1,], [1, 1]])

    res_idx = 1

    while res_idx < (n - 1):
        # Take the last list in res and use it to compose the next list

        last_list = res[res_idx].copy()  # avoid modifying original

        # pad with zeros at head and tail
        last_list.insert(0, 0)
        last_list.append(0)

        # set two pointers
        left_idx = 0
        right_idx = 1

        new = []
        while right_idx < len(last_list):
            # Populate `new` with the next list

            new.append(last_list[left_idx] + last_list[right_idx])
            left_idx += 1
            right_idx += 1

        res.append(new)
        res_idx += 1

    return res
