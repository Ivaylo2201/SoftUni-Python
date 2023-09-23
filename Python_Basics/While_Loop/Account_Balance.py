moneyList = []
while True:
    money = str(input())

    if money != 'NoMoreMoney':
        money = float(money)

        if money < 0:
            print('Invalid operation!')
            sumMoney = float(sum(moneyList))
            print(f"Total: {format(sumMoney, '.2f')}")
            quit()

        else:
            print(f"Increase: {format(money, '.2f')}")
            moneyList.append(money)

    elif money == 'NoMoreMoney':
        sumMoney = float(sum(moneyList))
        print(f"Total: {format(sumMoney, '.2f')}")
        quit()
