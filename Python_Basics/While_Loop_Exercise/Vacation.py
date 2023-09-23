moneyNeeded = float(input())
moneyAvailable = float(input())
days = 0
daysSpent = 0
while True:
    saveSpend = input()
    moneySavedSpent = float(input())

    if saveSpend == 'spend':
        days += 1
        daysSpent += 1

        if daysSpent >= 5:
            print("You can't save the money.")
            print(days)
            quit()

        if moneyAvailable - moneySavedSpent < 0:
            moneyAvailable = 0
        else:
            moneyAvailable -= moneySavedSpent
            continue

    if saveSpend == 'save':
        days += 1
        daysSpent = 0
        moneyAvailable += moneySavedSpent

        if moneyAvailable >= moneyNeeded:
            print(f"You saved the money for {days} days.")
            quit()
    continue
