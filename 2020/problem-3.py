with open('input/input-3.txt') as f:
    world = f.read().splitlines()

def use_slope(rt, dn):
    trees_hit = 0
    i = dn
    j = rt
    while i < len(world):
        if world[i][j] == '#':
            trees_hit += 1
        i += dn
        j = (j + rt) % len(world[0])
    return trees_hit

ans = use_slope(3, 1)
print("part 1:", ans)

ans *= use_slope(1, 1)
ans *= use_slope(5, 1)
ans *= use_slope(7, 1)
ans *= use_slope(1, 2)
print("part 2:", ans)
