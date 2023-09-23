listNums = list(map(int, input().split(" ")))
for i in range(len(listNums)):
    listNums[i] = -listNums[i]

print(listNums)
