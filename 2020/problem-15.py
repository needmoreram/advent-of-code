nums = "0,1,4,13,15,12,16".split(',')

d = {}
turn = 1
for n in nums[:-1]:
    d[int(n)] = turn
    turn += 1

last_spoken = int(nums[-1])
while turn < 30000000:
    if last_spoken not in d:
        speak = 0
        d[last_spoken] = turn
    else:
        speak = turn - d[last_spoken]
        d[last_spoken] = turn
    last_spoken = speak
    turn += 1
    if turn == 2020:
        print("part 1:", speak)
print("part 2:", speak) # lazy, yeah. i don't math well.
