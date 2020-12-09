import re

pws = []
with open('input-2.txt') as f:
    for line in f:
        pws.append(re.split("-| |: ", line))

num_valid = 0
for entry in pws:
    lo, hi, c, pw = entry
    n = pw.count(c)
    if n >= int(lo) and n <= int(hi):
        num_valid += 1
print("part 1:", num_valid)

num_valid = 0
for entry in pws:
    i, j, c, pw = entry
    i = int(i) - 1      # correct for 1-indexed
    j = int(j) - 1      # correct for 1-indexed
    if pw[i] == c or pw[j] == c:
        if pw[i] != pw[j]:
            num_valid += 1
print("part 2:", num_valid)
