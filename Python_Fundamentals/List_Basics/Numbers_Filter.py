n = int(input())
numsList = []

for _ in range(n):
    num = int(input())
    numsList.append(num)

listPositives = [numsList[x] for x in range(len(numsList)) if numsList[x] >= 0]
listNegatives = [numsList[x] for x in range(len(numsList)) if numsList[x] < 0]
listEven = [numsList[x] for x in range(len(numsList)) if numsList[x] % 2 == 0]
listOdd = [numsList[x] for x in range(len(numsList)) if numsList[x] % 2 != 0]

command = input()
if command == "even":
    print(listEven)
elif command == "odd":
    print(listOdd)
elif command == "negative":
    print(listNegatives)
elif command == "positive":
    print(listPositives)
