import numpy as np

with open('input-11.txt') as f:
    grid = f.read().splitlines()
    grid = list(map(list, grid))
    grid = np.array(grid)
    grid = np.pad(grid, 1, 'constant', constant_values=('.'))

def num_neighbour_seats(g, i, j):
    gs = g[i-1:i+2, j-1:j+2]
    n = len(gs[gs == '#'])
    n -= 1 if gs[1, 1] == '#' else 0
    assert n <= 8
    return n

not_stable = True
while not_stable:
    oldgrid = grid.copy()
    for i in range(1, grid.shape[0]-1):
        for j in range(1, grid.shape[1]-1):
            if grid[i, j] == '.':
                continue
            n = num_neighbour_seats(oldgrid, i, j)
            if n == 0:
                grid[i, j] = '#'
            elif n >= 4:
                grid[i, j] = 'L'
    if np.array_equal(oldgrid, grid):
        not_stable = False
print("part 1:", len(grid[grid == '#']))
