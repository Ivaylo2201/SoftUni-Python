rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

max_sum = 0
max_i, max_i1, max_j, max_j1 = 0, 0, 0, 0

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1] > max_sum:
            max_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]

            max_i = matrix[i][j]
            max_i1 = matrix[i][j+1]
            max_j = matrix[i+1][j]
            max_j1 = matrix[i+1][j+1]

print(max_i, max_i1)
print(max_j, max_j1)
print(max_sum)
