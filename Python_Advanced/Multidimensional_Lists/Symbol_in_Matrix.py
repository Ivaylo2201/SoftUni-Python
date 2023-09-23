matrix = []
n = int(input())

for rows in range(n):
    fill = list(input())
    matrix.append(fill)

symbol = input()

for index_row, row in enumerate(matrix):
    for index_col, col in enumerate(row):
        if col == symbol:
            print(f"({index_row}, {index_col})")
            exit()

print(f"{symbol} does not occur in the matrix")
