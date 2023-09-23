food = input()

foodType = ''
if food == 'banana' or food == 'apple' or food == 'kiwi' or food == 'cherry' or food == 'lemon' or food == 'grapes':
    foodType = 'fruit'
elif food == 'tomato' or food == 'cucumber' or food == 'pepper' or food == 'carrot':
    foodType = 'vegetable'
else:
    foodType = 'unknown'

print(foodType)
