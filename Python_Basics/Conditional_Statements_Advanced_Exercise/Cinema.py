projectionType = input()
rows = int(input())
columns = int(input())

total = 0
price = 0
if projectionType == 'Premiere':
    price = 12
elif projectionType == 'Normal':
    price = 7.5
elif projectionType == 'Discount':
    price = 5

total = price * (rows * columns)

print(f"{format(total, '.2f')}")
