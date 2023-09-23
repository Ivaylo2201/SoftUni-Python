from collections import deque

people = deque(input().split())
n = int(input())

move = 1
while len(people) > 1:
    if move % n != 0:
        people.append(people.popleft())
    else:
        print(f'Removed {people.popleft()}')
    move += 1

print(f'Last is {people.popleft()}')
