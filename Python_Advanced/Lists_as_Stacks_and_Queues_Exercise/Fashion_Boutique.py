from collections import deque

clothes = deque([int(x) for x in input().split()])
capacity = int(input())

racks = 1
current_rack_space = capacity

while clothes:
    cloth = clothes.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        racks += 1
        current_rack_space = capacity - cloth

print(racks)
