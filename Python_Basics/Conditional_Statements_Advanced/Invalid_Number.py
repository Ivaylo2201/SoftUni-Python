number = int(input())

result = ''
if number < 100 or number > 200:
    result = 'invalid'
if number == 0:
    result = ''

print(result)
