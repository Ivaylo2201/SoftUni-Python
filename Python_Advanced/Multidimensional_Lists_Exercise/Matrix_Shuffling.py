rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    row = input().split()
    matrix.append(row)

while True:
    command = input().split()

    if command[0] == 'END':
        break
    else:
        if command[0] == 'swap' and len(command) == 5:
            row1 = int(command[1])
            row2 = int(command[3])

            if row1 < 0 or row1 > rows - 1 or row2 < 0 or row2 > rows - 1:
                print('Invalid input!')
                continue

            col1 = int(command[2])
            col2 = int(command[4])

            if col1 < 0 or col1 > cols - 1 or col2 < 0 or col2 > cols - 1:
                print('Invalid input!')
                continue

            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for el in matrix:
                print(' '.join(el))
        else:
            print('Invalid input!')
