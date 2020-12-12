import numpy as np
from scipy.ndimage import convolve

with open('input-11.txt') as f:
    g = map(list, f.read().splitlines())
    g = np.array(list(g))
    dots = np.where(g == '.')
    grid = np.zeros(g.shape, np.int)

k = np.ones((3, 3))
k[1, 1] = 0

while True:
    c = convolve(grid, k, mode='constant', cval = 0)
    c[dots] = -1
    vacate = np.where(c >= 4)
    place = np.where(c == 0)
    if np.all(grid[vacate] == 0) and np.all(grid[place] == 1):
        break
    grid[vacate] = 0
    grid[place] = 1
print("part 1:", len(grid[grid == 1]))
