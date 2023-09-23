days = int(input())
nights = days - 1
roomType = input()
grade = input()
price = 0
if roomType == "room for one person":
    price = 18 * nights
elif roomType == "apartment":
    price = 25 * nights
    if nights < 10:
        price = price - 0.30 * price
    elif 10 <= nights <= 15:
        price = price - 0.35 * price
    elif nights >= 15:
        price = price - 0.50 * price
elif roomType == "president apartment":
    price = 35 * nights
    if nights < 10:
        price = price - 0.10 * price
    elif 10 <= nights <= 15:
        price = price - 0.15 * price
    elif nights >= 15:
        price = price - 0.20 * price
if grade == 'positive':
    price = price + 0.25 * price
elif grade == 'negative':
    price = price - 0.10 * price
print(format(price, '.2f'))
