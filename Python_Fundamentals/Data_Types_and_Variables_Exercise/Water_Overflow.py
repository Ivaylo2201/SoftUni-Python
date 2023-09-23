maxCapacity = 255
currentWater = 0

n = int(input())
for _ in range(n):
    water = int(input())
    if currentWater + water > maxCapacity:
        print("Insufficient capacity!")
    else:
        currentWater += water
print(currentWater)
