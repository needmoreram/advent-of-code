actions = []
with open('input/input-12.txt') as f:
    for line in f:
        actions.append((line[0], int(line[1:])))

def execute(actions, wpt, part2=False):
    pos = [0, 0]
    for inst, val in actions:
        if inst == 'F':
            pos[0] += wpt[0] * val
            pos[1] += wpt[1] * val
        elif inst in "RL":
            f = 1 if inst == 'L' else -1
            for i in range(int(val / 90) % 4):
                wpt = [-f * wpt[1], f * wpt[0]]
        else:
            ch = wpt if part2 else pos
            if   inst == 'N': ch[1] += val
            elif inst == 'S': ch[1] -= val
            elif inst == 'E': ch[0] += val
            elif inst == 'W': ch[0] -= val
    return sum(map(abs, pos))

print("part 1:", execute(actions, [1, 0]))
print("part 2:", execute(actions, [10, 1], True))
