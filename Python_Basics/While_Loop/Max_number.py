numList = []
while True:
    num = str(input())

    if num != 'Stop':
        numList.append(int(num))
    else:
        maxNum = max(numList)
        print(maxNum)
        quit()
