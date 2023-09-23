matrix = []

n = int(input())
for rows in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

sum_diagonal = 0
index = 0

for row in matrix:
    sum_diagonal += row[index]
    index += 1

print(sum_diagonal)
