numCount = int(input())
numCountX2 = numCount * 2
numListLeft = []
numListRight = []
for i in range(numCount):
    numLeft = int(input())
    numListLeft.append(numLeft)

for u in range(numCount):
    numRight = int(input())
    numListRight.append(numRight)

sumLeft = sum(numListLeft)
sumRight = sum(numListRight)

if sumLeft == sumRight:
    print(f"Yes, sum = {sumLeft}")
elif sumLeft > sumRight or sumLeft < sumRight:
    diff = abs(sumLeft - sumRight)
    print(f"No, diff = {diff}")
