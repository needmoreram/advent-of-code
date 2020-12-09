with open('input-8.txt') as f:
	program = f.read().splitlines()

def expgm(program):
	pc = 0
	acc = 0
	seen = set()

	while pc not in seen and pc < len(program):
		inst, arg = program[pc].split(' ')
		seen.add(pc)
		if inst == 'jmp':
			pc += int(arg)
			continue
		elif inst == 'acc':
			acc += int(arg)
		elif inst == 'nop':
			pass
		else:
			raise ValueError
		pc += 1

	return pc, acc

pc, acc = expgm(program)
print("part 1:", acc)
program[pc] = program[pc].replace("jmp", "nop")
pc, acc = expgm(program)
print("part 2:", acc)