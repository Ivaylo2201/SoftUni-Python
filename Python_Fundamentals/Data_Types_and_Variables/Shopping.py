budget = int(input())
while True:
    itemPrice = input()
    if itemPrice == "End":
        print("You bought everything needed.")
        break
    else:
        budget -= int(itemPrice)
        if budget < 0:
            print("You went in overdraft!")
            break
        else:
            continue
