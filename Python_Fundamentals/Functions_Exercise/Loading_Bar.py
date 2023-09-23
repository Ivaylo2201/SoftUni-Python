def Loading_bar(num):
    barList = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    percents = num // 10

    for i in range(percents):
        barList[i] = '%'

    stringBar = ''.join(barList)
    return stringBar


result = None
n = int(input())

if n == 100:
    result = f"{n}% Complete!"
    print(result)
    print(f"[{Loading_bar(n)}]")
else:
    result = "Still loading..."
    print(f"{n}% [{Loading_bar(n)}]")
    print(result)
