#!/usr/bin/python3
"""Backtracking the nqueens puzzle.
"""
import sys

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    grid_size = int(sys.argv[1])
    if grid_size < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)


def resolve_nqueens(grid_size):
    """Implements a solution to the nqueens problem.
    """
    col = set()
    pos_diagonal = set()
    neg_diagonal = set()

    solution = []
    tmp_solution = [[] for _ in range(grid_size)]

    def backtrack(row_idx):
        """The recursive implementation.
        """
        if row_idx == grid_size:
            # base case; end of grid,
            # ...whose end could be reached again for another solution
            solution.append([coord.copy() for coord in tmp_solution])
            return

        for col_idx in range(grid_size):
            if col_idx in col or\
                    (row_idx + col_idx) in pos_diagonal or\
                    (row_idx - col_idx) in neg_diagonal:
                # current cell in susceptible to attack
                continue

            # otherwise add cells to exclude
            col.add(col_idx)
            pos_diagonal.add(row_idx + col_idx)
            neg_diagonal.add(row_idx - col_idx)
            # track [potentially] valid coordinate
            tmp_solution[row_idx].append(row_idx)
            tmp_solution[row_idx].append(col_idx)
            # print(tmp_solution)

            # recurse for next row
            backtrack(row_idx + 1)

            # no valid path found, or after last grid row;
            # ...remove last saved potential coordinate, and column index
            col.remove(col_idx)
            pos_diagonal.remove(row_idx + col_idx)
            neg_diagonal.remove(row_idx - col_idx)
            tmp_solution[row_idx].clear()

    backtrack(0)
    return solution


for solution in resolve_nqueens(grid_size):
    print(solution)
