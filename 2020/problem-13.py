with open('input/input-13.txt') as f:
    arrival_ts = int(f.readline())
    bus_ids = []
    for id in f.readline().split(','):
        if id != 'x':
            bus_ids.append(int(id))

ans = None
best = max(bus_ids)
for id in bus_ids:
    v = (id - (arrival_ts % id)) % id
    if v < best:
        ans = id
        best = v
print("part 1:", ans * best)
