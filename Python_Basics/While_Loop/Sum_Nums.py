num = int(input())
sumList = []
while True:
    num2 = int(input())
    sumList.append(num2)

    if sum(sumList) >= num:
        print(sum(sumList))
        quit()
