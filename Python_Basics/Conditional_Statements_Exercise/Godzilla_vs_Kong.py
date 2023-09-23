movieBudget = float(input())
statistCount = int(input())
OutfitPriceOneStatist = float(input())
movieDecoration = movieBudget * 0.10
statistsOutfitPrice = statistCount * OutfitPriceOneStatist
if statistCount >= 150:
    statistsOutfitPrice = statistsOutfitPrice - statistsOutfitPrice * 0.10
sumTotal = movieDecoration + statistsOutfitPrice
if movieBudget >= sumTotal:
    print("Action!")
    print(f"Wingard starts filming with {format(movieBudget - sumTotal, '.2f')} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {format(sumTotal - movieBudget, '.2f')} leva more.")
