with open('input/input-5.txt') as f:
    seats = f.read().splitlines()

d = []
max_seat_id = 0
for seat in seats:
    seat = seat.replace('F', '0')
    seat = seat.replace('B', '1')
    seat = seat.replace('L', '0')
    seat = seat.replace('R', '1')
    row = int(seat[:7], 2)
    col = int(seat[7:], 2)
    assert row < 128 and col < 8
    seat_id = row * 8 + col
    d.append(seat_id)
    if seat_id > max_seat_id:
        max_seat_id = seat_id
print('part 1:', max_seat_id)

for i in range(128 * 8):
    if i not in d:
        if i-1 in d and i+1 in d:
            print('part 2:', i)
            break
