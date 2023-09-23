rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

matrix_sum = 0
for el in matrix:
    for num in el:
        matrix_sum += num

print(matrix_sum)
print(matrix)
