lostFights = int(input())
helmetPrice = float(input())
swordPrice = float(input())
shieldPrice = float(input())
armorPrice = float(input())

total = 0
shieldBroken = 0

for i in range(1, lostFights + 1):
    if i % 2 == 0:
        total += helmetPrice
    if i % 3 == 0:
        total += swordPrice
        if i % 2 == 0:
            total += shieldPrice
            shieldBroken += 1
            if shieldBroken % 2 == 0:
                total += armorPrice

print(f"Gladiator expenses: {format(total, '.2f')} aureus")
