with open('input/input-14.txt') as f:
    program = f.read().splitlines()

mem = {}
for line in program:
    lval, rval = line.split(' = ')
    if lval == 'mask':
        set_mask = int(rval.replace('X', '0'), 2)
        clear_mask = int(rval.replace('X', '1'), 2)
    else:
        rval = int(rval) | set_mask
        rval &= clear_mask
        exec(lval + " = " + str(rval))

ans = 0
for loc in mem:
    ans += mem[loc]
print("part 1:", ans)
