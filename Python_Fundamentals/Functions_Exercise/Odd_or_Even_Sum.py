def Sums(n):
    listEven = []
    listOdd = []

    nString = str(n)
    for i in range(len(nString)):
        if int(nString[i]) % 2 == 0:
            listEven.append(int(nString[i]))
        else:
            listOdd.append(int(nString[i]))

    print(f"Odd sum = {sum(listOdd)}, Even sum = {sum(listEven)}")


num = int(input())
Sums(num)
