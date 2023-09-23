from collections import deque

food_quantity = int(input())

queue = deque()

nums = [int(x) for x in input().split()]
for i in nums:
    queue.append(i)

print(max(queue))
while queue:
    order = int(queue[0])
    if food_quantity - order >= 0:
        food_quantity -= order
        queue.popleft()
    else:
        break

if len(queue) == 0:
    print('Orders complete')
else:
    print('Orders left: ', end='')
    for _ in range(len(queue)):
        print(queue.popleft(), end=' ')
