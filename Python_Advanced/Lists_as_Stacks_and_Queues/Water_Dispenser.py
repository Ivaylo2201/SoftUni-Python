from collections import deque
queue = deque([])

water_quantity = int(input())
while True:
    name = input()

    if name == 'Start':
        break
    else:
        queue.append(name)

while True:
    command = input().split()
    if command[0] == 'End':
        break
    else:
        if command[0] == 'refill':
            liters = int(command[1])
            water_quantity += liters
        else:
            requested_water = int(command[0])
            if requested_water <= water_quantity:
                water_quantity -= requested_water
                print(f"{queue.popleft()} got water")
            else:
                print(f"{queue.popleft()} must wait")

print(f"{water_quantity} liters left")
