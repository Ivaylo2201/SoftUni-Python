rows, cols = [int(x) for x in input().split()]
matrix = []
sq_matrices = 0

for _ in range(rows):
    row = input().split()
    matrix.append(row)

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            sq_matrices += 1

print(sq_matrices)
