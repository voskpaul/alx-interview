#!/usr/bin/python3
"""
This module defines the function island_perimeter.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    Args:
        grid (list of list of int): 2D grid where 0 is water and 1 is land.
    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4
                # Subtract 2 for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:  # Up
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 2

    return perimeter

