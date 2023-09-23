factor = int(input())
count = int(input())
numsList = []
i = factor

while len(numsList) != count:
    if i % factor == 0:
        numsList.append(i)
    i += 1

print(numsList)
