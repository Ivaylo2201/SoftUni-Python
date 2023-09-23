nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
bonusNylon = 2 * 1.50
bonusBags = 0.40
paintPriceFirst = paint * 14.50
nylonPrice = (nylon * 1.50) + bonusNylon
paintPriceSecond = paintPriceFirst + paintPriceFirst * 0.10
thinnerPrice = thinner * 5
sumBefore = nylonPrice + paintPriceSecond + thinnerPrice + bonusBags
workersPay = (0.30 * sumBefore)*hours
finalSum = sumBefore + workersPay
print(finalSum)
