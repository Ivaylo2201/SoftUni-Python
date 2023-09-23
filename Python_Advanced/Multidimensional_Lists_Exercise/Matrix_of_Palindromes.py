rows, cols = [int(x) for x in input().split()]
matrix = []
index_primary = 97

for _ in range(rows):
    row = []

    char = list(chr(index_primary) * 3)
    row.append(''.join(char))
    index_middle = index_primary

    for _ in range(cols - 1):
        char[1] = chr(index_middle + 1)
        row.append(''.join(char))
        index_middle += 1

    matrix.append(row)
    index_primary += 1

for el in matrix:
    print(' '.join(el))
