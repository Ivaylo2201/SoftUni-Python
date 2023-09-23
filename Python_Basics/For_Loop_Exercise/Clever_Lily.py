age = int(input())
washing_machinePrice = float(input())
toyPrice = int(input())

moneyList = []
toyList = []
startingMoney = 10

if age % 2 == 0:
    for i in range(age):
        if i % 2 == 0:
            moneyList.append(startingMoney - 1)
            startingMoney += 10
        else:
            toyList.append(toyPrice)

else:
    toyList.append(toyPrice)
    for i in range(age - 1):
        if i % 2 == 0:
            moneyList.append(startingMoney - 1)
            startingMoney += 10
        else:
            toyList.append(toyPrice)

toyMoney = len(toyList) * toyPrice
total = sum(moneyList) + toyMoney

if total >= washing_machinePrice:
    print(f"Yes! {format(total - washing_machinePrice, '.2f')}")
elif total < washing_machinePrice:
    print(f"No! {format(washing_machinePrice - total, '.2f')}")
