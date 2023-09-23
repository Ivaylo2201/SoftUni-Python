from collections import deque

n, m = [int(x) for x in input().split()]
text_const = input()
text = deque(text_const)
matrix = [[] for _ in range(n)]

for el in matrix:
    for i in range(m):
        if len(text) > 0:
            el.append(text.popleft())
        else:
            text = deque(text_const)
            el.append(text.popleft())

for i in range(0, len(matrix)):
    if (i + 1) % 2 == 0:
        reversed_str = ''.join(matrix[i])
        print(reversed_str[::-1])
    else:
        print(''.join(matrix[i]))
