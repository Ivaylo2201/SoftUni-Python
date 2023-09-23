numsString = input().split()
numsInt = [int(x) for x in numsString]
timeFirst = 0
timeSecond = 0

middle = len(numsInt) // 2
firstCar = numsInt[0:middle]
secondCar = numsInt[middle+1:]

for i in firstCar:
    if i != 0:
        timeFirst += i
    else:
        timeFirst *= 0.8

for i in reversed(secondCar):
    if i != 0:
        timeSecond += i
    else:
        timeSecond *= 0.8

if timeFirst < timeSecond:
    print(f"The winner is left with total time: {format(timeFirst, '.1f')}")
else:
    print(f"The winner is right with total time: {format(timeSecond, '.1f')}")
