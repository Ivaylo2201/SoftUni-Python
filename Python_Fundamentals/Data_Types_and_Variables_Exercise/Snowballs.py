listValue = []
listWeight = []
listTime = []
listQuality = []

n = int(input())
for i in range(n):
    snowballWeight = int(input())
    listWeight.append(snowballWeight)
    timeNeeded = int(input())
    listTime.append(timeNeeded)
    snowballQuality = int(input())
    listQuality.append(snowballQuality)

    snowballValue = int((snowballWeight / timeNeeded) ** snowballQuality)
    listValue.append(snowballValue)

bestSnowballInd = listValue.index(max(listValue))
print(f"{listWeight[bestSnowballInd]} : {listTime[bestSnowballInd]} = {listValue[bestSnowballInd]} ({listQuality[bestSnowballInd]})")
