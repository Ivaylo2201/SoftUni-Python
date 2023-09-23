numList = []
while True:
    num = str(input())

    if num != 'Stop':
        numList.append(int(num))
    else:
        minNum = min(numList)
        print(minNum)
        quit()
