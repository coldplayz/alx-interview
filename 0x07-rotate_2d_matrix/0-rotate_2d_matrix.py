#!/usr/bin/python3
""" Rotate a matrix 90 deg.
"""


def rotate_2d_matrix(matrix):
    """ Rotate matrix by 90deg in-place.

    Args:
        - matrix (list[list]): a list of lists.
    Returns:
        - None
    Assumptions:
        - the matrix will have two dimensions.
        - the matrix will not be empty.
    """
    # first reverse the rows in matrix
    matrix.reverse()

    # calculate number of rows and columns in final matrix
    # dimensions of the final matrix should be inverse that of the original
    rows = len(matrix)
    cols = len(matrix[0])

    # number of rows of final matrix should be same as number of cols of orig
    ll90 = [[] for _ in range(cols)]  # tmp proxy for matrix

    # to form new rows, append all items of a particular column in the...
    # ...original matrix, to the corresponding row in the final matrix - ll90
    for c_idx in range(cols):
        for r_idx in range(rows):
            ll90[c_idx].append(matrix[r_idx][c_idx])

    # clear all lists in matrix for in-place edit
    for arr in matrix:
        arr.clear()

    # copy ll90 (list-of-lists-90deg) lists to cleared matrix list
    # for rectangular matrices, empty lists are bound to remain in matrix
    for idx in range(len(ll90)):
        matrix[idx].extend(ll90[idx])

    # remove remaining empty list(s) in rectangular matrices
    try:
        matrix.remove([])
    except ValueError:
        pass


'''
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ]

matrix2 = [
        [1, 2],
        [3, 4],
        [5, 6],
        ]

print(matrix2)
print(rotate_2d_matrix(matrix2))
'''
