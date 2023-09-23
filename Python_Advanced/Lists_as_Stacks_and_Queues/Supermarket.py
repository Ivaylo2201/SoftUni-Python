from collections import deque

queue = deque([])

while True:
    client = input()
    if client == 'End':
        break
    elif client == 'Paid':
        while len(queue) > 0:
            print(queue.popleft())
    else:
        queue.append(client)

print(f"{len(queue)} people remaining.")
