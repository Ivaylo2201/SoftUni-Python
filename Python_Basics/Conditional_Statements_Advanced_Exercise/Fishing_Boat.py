groupBudget = int(input())
season = input()
fishermenCount = int(input())
boatPrice = 0
if season == 'Spring':
    boatPrice = 3000
elif season == 'Summer' or season == 'Autumn':
    boatPrice = 4200
elif season == 'Winter':
    boatPrice = 2600
if fishermenCount <= 6:
    boatPrice = boatPrice - boatPrice * 0.10
elif 7 <= fishermenCount <= 11:
    boatPrice = boatPrice - boatPrice * 0.15
elif fishermenCount >= 12:
    boatPrice = boatPrice - boatPrice * 0.25
if fishermenCount % 2 == 0 and season != 'Autumn':
    boatPrice = boatPrice - boatPrice * 0.05
if groupBudget >= boatPrice:
    print(f"Yes! You have {format(groupBudget - boatPrice, '.2f')} leva left.")
else:
    print(f"Not enough money! You need {format(boatPrice - groupBudget, '.2f')} leva.")
