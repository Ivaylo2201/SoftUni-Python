n_guests = int(input())

reservations = set()

for _ in range(n_guests):
    code = input()
    reservations.add(code)

while True:
    guests_code = input()
    if guests_code == 'END':
        break
    else:
        reservations.remove(guests_code)

print(len(reservations))
for guest in sorted(reservations):
    print(guest)
