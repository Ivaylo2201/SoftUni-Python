parking_lot = set()
n_commands = int(input())

for _ in range(n_commands):
    data = tuple(input().split(', '))

    direction, car_number = data

    if direction == 'IN':
        parking_lot.add(car_number)
    elif direction == 'OUT':
        parking_lot.remove(car_number)

if len(parking_lot) == 0:
    print('Parking Lot is Empty')
else:
    for car in parking_lot:
        print(car)
