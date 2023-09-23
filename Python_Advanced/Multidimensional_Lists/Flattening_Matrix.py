rows = int(input())
matrix = []
result = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

for el in matrix:
    for num in el:
        result.append(num)

print(result)
