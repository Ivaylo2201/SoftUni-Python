while True:
    moneyList = []
    destination = input()
    if destination == 'End':
        quit()

    budget = float(input())

    for i in range(int(budget)):
        money = input()
        moneyList.append(float(money))

        if sum(moneyList) >= budget:
            print(f"Going to {destination}!")
            break
