groupSize = int(input())
days = int(input())
coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        groupSize -= 2
    if i % 15 == 0:
        groupSize += 5
    coins += 50 - groupSize * 2
    if i % 3 == 0:
        coins -= groupSize * 3
    if i % 5 == 0:
        coins += groupSize * 20
        if i % 3 == 0:
            coins -= groupSize * 2

print(f"{groupSize} companions received {int(coins/groupSize)} coins each.")
