string = input()
vowels = ['a', 'o', 'u', 'e', 'i']

newString = [x for x in string if x not in vowels]
print(''.join(newString))
