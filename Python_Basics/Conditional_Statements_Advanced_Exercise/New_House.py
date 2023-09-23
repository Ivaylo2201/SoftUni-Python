flowerType = input()
flowerCount = int(input())
budget = int(input())

price = 0
if flowerType == 'Roses':
    price = flowerCount * 5
if flowerType == 'Dahlias':
    price = flowerCount * 3.8
if flowerType == 'Tulips':
    price = flowerCount * 2.8
if flowerType == 'Narcissus':
    price = flowerCount * 3
if flowerType == 'Gladiolus':
    price = flowerCount * 2.5

if flowerType == 'Roses' and flowerCount > 80:
    price = price - price * 0.10
if flowerType == 'Dahlias' and flowerCount > 90:
    price = price - price * 0.15
if flowerType == 'Tulips' and flowerCount > 80:
    price = price - price * 0.15
if flowerType == 'Narcissus' and flowerCount < 120:
    price = price + price * 0.15
if flowerType == 'Gladiolus' and flowerCount < 80:
    price = price + price * 0.20

if budget >= price:
    print(
        f"Hey, you have a great garden with {flowerCount} {flowerType} and {format(budget - price, '.2f')} leva left.")
else:
    print(f"Not enough money, you need {format(price - budget, '.2f')} leva more.")
