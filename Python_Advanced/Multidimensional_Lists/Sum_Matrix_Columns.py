rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

index = 0

for _ in range(cols):
    col_sum = 0
    for el in matrix:
        col_sum += el[index]
    index += 1
    print(col_sum)
