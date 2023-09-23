rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
final_matrix = []

result = 0
sum_matrix = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        mini_matrix = [
            matrix[row][col], matrix[row][col+1], matrix[row][col+2],
            matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2],
            matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]
        ]

        sum_matrix = sum(mini_matrix)

        if sum_matrix >= result:
            result = sum_matrix

            final_matrix = [
                [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
            ]

print(f'Sum = {result}')
if final_matrix:
    for el in final_matrix:
        print(' '.join([str(x) for x in el]))
