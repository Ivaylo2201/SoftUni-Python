tripPrice = float(input())
puzzlesCount = int(input())
dollsCount = int(input())
teddiesCount = int(input())
minionsCount = int(input())
trucksCount = int(input())
grandTotal = 0
rent = 0
sumTotal = puzzlesCount * 2.60 + dollsCount * 3 + teddiesCount * 4.10 + minionsCount * 8.20 + trucksCount * 2
if puzzlesCount + dollsCount + teddiesCount + minionsCount + trucksCount >= 50:
    sumTotal = sumTotal - sumTotal * 0.25
rent = sumTotal * 0.10
grandTotal = sumTotal - rent
if grandTotal >= tripPrice:
    print(f"Yes! {format(grandTotal - tripPrice, '.2f')} lv left.")
else:
    print(f"Not enough money! {format(tripPrice - grandTotal, '.2f')} lv needed.")
