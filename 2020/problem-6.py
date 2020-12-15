with open('input/input-6.txt') as f:
    groups = f.read().split('\n\n')

sum_any = 0
sum_all = 0
for group in groups:
    g = group.split('\n')
    sl = set(''.join(g))
    sum_any += len(sl)
    for p in g:
        sl &= set(p)
    sum_all += len(sl)
print("part 1:", sum_any)
print("part 2:", sum_all)
