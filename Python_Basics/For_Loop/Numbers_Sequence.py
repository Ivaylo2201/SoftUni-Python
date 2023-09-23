numCount = int(input())
numList = []
for i in range(numCount):
    num = int(input())
    numList.append(num)
print(f"Max number: {max(numList)}")
print(f"Min number: {min(numList)}")
