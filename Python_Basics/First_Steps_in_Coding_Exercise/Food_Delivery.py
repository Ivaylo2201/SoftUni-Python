chickenMenus = int(input())
fishMenus = int(input())
veganMenus = int(input())

delivery = 2.50
foodSumNoDessert = (chickenMenus * 10.35) + (fishMenus * 12.40) + (veganMenus * 8.15)
dessert = 0.20 * foodSumNoDessert
foodSumWithDessert = foodSumNoDessert + dessert + delivery
print(foodSumWithDessert)
