#!/usr/bin/python3
""" Calculate an island's perimeter.
"""


def island_perimeter(grid):
    """ Determine the perimeter of grid.

    Args:
    -----
        - grid (list[list[int]]): a list of list of integers.

    Assumptions/facts:
    ------------------
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally).
        - grid is rectangular, with its width and height not exceeding 100
        - The grid is completely surrounded by water
        - The island doesn't have lakes, i.e. water inside that
          ...isn't connected to the water surrounding the island

    Returns:
    --------
        - int: the perimeter of the island
    """
    if not isinstance(grid, list) or len(grid) == 0:
        return 0

    perimeter = 0
    water_tiles = []  # list of strings
    land_tiles = {}  # dict of dicts

    # determine how many rows in grid, and cols in each row
    row_num = len(grid)
    col_num = len(grid[0])

    # traverse each row in grid, mapping water amd land tiles
    for row in range(row_num):
        for col in range(col_num):
            if grid[row][col] == 0:
                # water; save a unique identifier for the cell
                cell_id = 'r{}c{}'.format(row, col)
                water_tiles.append(cell_id)
            else:
                # land tile
                cell_id = 'r{}c{}'.format(row, col)
                # save row and column numbers
                dct = dict(row=row, col=col)
                land_tiles.update({cell_id: dct})

    # process mapped data
    for dct in land_tiles.values():
        row = dct['row']
        col = dct['col']

        # search for water in row above (if any)
        row_above = row - 1
        cell_id = 'r{}c{}'.format(row_above, col)
        if cell_id in water_tiles:
            perimeter += 1

        # search for water in row below (if any)
        row_below = row + 1
        cell_id = 'r{}c{}'.format(row_below, col)
        if cell_id in water_tiles:
            perimeter += 1

        # search for water in left col (if any)
        left_col = col - 1
        cell_id = 'r{}c{}'.format(row, left_col)
        if cell_id in water_tiles:
            perimeter += 1

        # search for water in right col (if any)
        right_col = col + 1
        cell_id = 'r{}c{}'.format(row, right_col)
        if cell_id in water_tiles:
            perimeter += 1

    return perimeter
