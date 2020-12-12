import numpy as np
from scipy.ndimage import convolve

with open('input-11.txt') as f:
    grid = map(list, f.read().splitlines())
    grid = np.array(list(grid))
    ng = np.zeros(grid.shape, np.int)

k = np.ones((3, 3))
k[1, 1] = 0

while True:
    c = convolve(ng, k, mode='constant', cval = 0)
    c[np.where(grid == '.')] = -1
    vacate = np.where(c >= 4)
    place = np.where(c == 0)
    if np.all(ng[vacate] == 0) and np.all(ng[place] == 1):
        break
    grid[vacate] = 'L'
    ng[vacate] = 0
    grid[place] = '#'
    ng[place] = 1
print("part 1:", len(grid[grid == '#']))
