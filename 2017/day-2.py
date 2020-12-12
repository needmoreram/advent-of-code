from operator import methodcaller

sheet = []
with open('input/input-2.txt') as f:
    for line in f:
        sheet.append([int(x) for x in line.split()])

ans = 0
for line in sheet:
    ans += (max(line) - min(line))
print("part 1:", ans)
