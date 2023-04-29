#Minesweeper task 

import itertools

#This code generates a minefield where each cell shows the number of neighboring mines, given an input grid with "#" representing a mine and "-" representing an empty cell.
def generate_minefield(grid):
    minefield = []
    for i in range(len(grid)):
        minefield.append(grid[i][:])
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                continue
            minefield[i][j] = count_neighbors(grid, i, j)
    return minefield

# defines a function called count_neighbors that takes a grid, row, and col as inputs and counts the number of neighboring cells that contain the character
def count_neighbors(grid, row, col):
    directions = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    directions.remove((0, 0))
    
    neighbors = 0
    for d in directions:
        r, c = row + d[0], col + d[1]
        if 0 <= r < len(grid) and 0 <= c < len(grid[row]) and grid[r][c] == '#':
            neighbors += 1
    return neighbors


grid = [['#', '-', '-', '#', '#'],
        ['-', '#', '#', '-', '-'],
        ['#', '#', '-', '-', '-'],
        ['-', '#', '-', '#', '-'],
        ['-', '#', '#', '#', '-']]

mines = generate_minefield(grid)

#Prints new grid 
for count, mines in enumerate(mines, start=0):
    print(f'{mines}')
