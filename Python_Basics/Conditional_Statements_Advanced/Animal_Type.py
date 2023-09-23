animal = input()
animalClass = ''
if animal == 'dog':
    animalClass = 'mammal'
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    animalClass = 'reptile'
else:
    animalClass = 'unknown'
print(animalClass)
