with open('input/input-8.txt') as f:
    program = f.read().splitlines()

def expgm(program):
    pc = acc = 0
    seen = set()

    while pc not in seen and pc < len(program):
        seen.add(pc)
        inst, arg = program[pc].split(' ')
        if inst == 'jmp':
            pc += int(arg) - 1
        elif inst == 'acc':
            acc += int(arg)
        pc += 1

    return pc, acc, seen

pc, acc, seen = expgm(program)
print("part 1:", acc)
for inum in seen:
    if 'acc' in program[inum]:
        continue
    pmod = program.copy()
    if 'jmp' in program[inum]:
        pmod[inum] = pmod[inum].replace('jmp', 'nop')
    elif 'nop' in program[inum]:
        pmod[inum] = pmod[inum].replace('nop', 'jmp')
    pc, acc, _ = expgm(pmod)
    if pc >= len(program):
        print("part 2:", acc)
