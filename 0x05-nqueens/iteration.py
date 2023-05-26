#!/usr/bin/python3
"""Backtracking the nqueens puzzle, using iteration.
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
    """Implements an iterative solution to the nqueens problem.

    Backtracking to a previous row here involves
    ...clearing saved valid cell info for the previous row,
    ...and moving to/continuing with the next cell in this previous row.
    """
    cols = set()
    pos_diagonal = set()
    neg_diagonal = set()

    rn = 0
    cn = 0
    rc = {-1: None}  # for remembering next column of previous row

    sln = []
    t_sln = [[] for _ in range(grid_size)]

    while 0 <= rn < grid_size:
        while cn < grid_size:
            if cn in cols or\
                    (rn + cn) in pos_diagonal or\
                    (rn - cn) in neg_diagonal:
                # current cell is susceptible to attack, goto next column
                cn += 1
                continue

            # valid cell; add to exclusion sets
            cols.add(cn)
            pos_diagonal.add(rn + cn)
            neg_diagonal.add(rn - cn)
            t_sln[rn].extend([rn, cn])  # save its coordinates
            rc.update({rn: cn + 1})  # save next column
            break

        if cn >= grid_size:
            # backtrack to previous row
            cn = rc[rn - 1]
            if cn is None:
                # prev_rn === -1; base case/end of algorithm
                break
            prev_rn = rn - 1
            prev_cn = cn - 1
            # remove previously valid cell
            cols.remove(prev_cn)
            pos_diagonal.remove(prev_rn + prev_cn)
            neg_diagonal.remove(prev_rn - prev_cn)
            t_sln[prev_rn].clear()
            rn = prev_rn
            continue

        # no backtracking required most times; goto next row
        if rn == grid_size - 1:
            # last row; a solution found; save it
            sln.append([coord.copy() for coord in t_sln])
            # check for other solutions by backtracking...sort of
            # clear saved valid cell for current/last row (grid_size - 1)
            cols.remove(cn)
            pos_diagonal.remove(rn + cn)
            neg_diagonal.remove(rn - cn)
            t_sln[rn].clear()
            # backtrack to previous row (grid_size - 2)
            prev_next_cn = rc[rn - 1]
            prev_rn = rn - 1
            prev_cn = prev_next_cn - 1
            cols.remove(prev_cn)
            pos_diagonal.remove(prev_rn + prev_cn)
            neg_diagonal.remove(prev_rn - prev_cn)
            t_sln[prev_rn].clear()
            rn = prev_rn
            cn = prev_next_cn
            continue
        # not last row yet; goto next row
        rn += 1
        cn = 0

    return sln


for solution in resolve_nqueens(grid_size):
    print(solution)
