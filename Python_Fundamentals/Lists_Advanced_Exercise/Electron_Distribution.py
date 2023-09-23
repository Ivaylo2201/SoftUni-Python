electrons = int(input())
electronList = []

for i in range(1, electrons+1):
    if electrons <= 0:
        break
    else:
        occupied = 2*i**2
        if occupied > electrons:
            electronList.append(electrons)
        else:
            electronList.append(occupied)
        electrons -= occupied

print(electronList)
