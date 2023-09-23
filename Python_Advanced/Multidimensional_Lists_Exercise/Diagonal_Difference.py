n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary_diagonal = []
secondary_diagonal = []

index = 0
for el in matrix:
    primary_diagonal.append(el[index])
    index += 1

index = n - 1
for el in matrix:
    secondary_diagonal.append(el[index])
    index -= 1

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
