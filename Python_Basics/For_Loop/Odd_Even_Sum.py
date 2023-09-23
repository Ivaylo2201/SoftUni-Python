numCount = int(input())
numList = []

for e in range(numCount):
    number = int(input())
    numList.append(number)

odd_i = []
even_i = []
for i in range(0, len(numList)):
    if i % 2:
        even_i.append(numList[i])
    else:
        odd_i.append(numList[i])

sumOdd = sum(odd_i)
sumEven = sum(even_i)

if sumOdd == sumEven:
    print("Yes")
    print(f"Sum = {sumEven}")
elif sumOdd > sumEven or sumOdd < sumEven:
    diff = abs(sumOdd - sumEven)
    print("No")
    print(f"Diff = {diff}")
