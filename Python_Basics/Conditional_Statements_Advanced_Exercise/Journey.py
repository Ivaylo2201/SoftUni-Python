budget = float(input())
season = input()

price = 0
home = ''
if budget <= 100:
    if season == 'summer':
        price = budget * 0.30
        home = 'Camp'
    elif season == 'winter':
        price = budget * 0.70
        home = 'Hotel'
elif budget <= 1000:
    if season == 'summer':
        price = budget * 0.40
        home = 'Camp'
    elif season == 'winter':
        price = budget * 0.80
        home = 'Hotel'
elif budget > 1000:
    price = budget * 0.90
    home = 'Hotel'

if budget <= 100:
    print("Somewhere in Bulgaria")
    print(f"{home} - {format(price,'.2f')}")
elif budget <= 1000:
    print("Somewhere in Balkans")
    print(f"{home} - {format(price,'.2f')}")
elif budget > 1000:
    print("Somewhere in Europe")
    print(f"{home} - {format(price,'.2f')}")
