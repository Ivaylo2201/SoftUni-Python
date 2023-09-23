def Order(item, quantity):
    price = 0
    if item == "coffee":
        price += quantity * 1.50
    elif item == "water":
        price += quantity * 1.00
    elif item == "coke":
        price += quantity * 1.40
    elif item == "snacks":
        price += quantity * 2.00
    return price


product = input()
n = int(input())
print(format(Order(product, n), '.2f'))
