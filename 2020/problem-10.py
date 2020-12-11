with open('input-10.txt') as f:
    adaps = [0] + list(map(int, f.read().splitlines()))
    adaps.sort()

diffs = [0] * 4
for i in range(1, len(adaps)):
    d = adaps[i] - adaps[i-1]
    diffs[d] += 1
diffs[3] += 1 # difference to device counts too
print("part 1:", diffs[1] * diffs[3])
print(adaps)
