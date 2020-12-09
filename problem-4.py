with open('input-4.txt') as f:
    passports = f.read().split('\n\n')

valid_entries = 0
for entry in passports:
    c = entry.count(':')
    if c == 8:
        valid_entries += 1
    elif c == 7:
        if 'cid:' not in entry:
            valid_entries += 1
print("part 1:", valid_entries)
