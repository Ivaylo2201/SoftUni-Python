orders = {}
while True:
    product = input().split()
    if product[0] == 'buy':
        break
    else:
        if product[0] not in orders:
            orders[product[0]] = [float(product[1]), int(product[2])]
        else:
            orders[product[0]][1] += int(product[2])
            if orders[product[0]][0] != float(product[1]):
                orders[product[0]][0] = float(product[1])

for key, value in orders.items():
    print(f"{key} -> {format(orders[key][0] * orders[key][1], '.2f')}")
