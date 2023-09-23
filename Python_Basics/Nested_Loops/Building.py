floors = int(input())
rooms = int(input())
listBuilding = []

for f in range(1, floors + 1):
    for r in range(0, rooms):

        if f % 2 == 0:
            if f == floors:
                listBuilding.append(f"L{f}{r}")
            else:
                listBuilding.append(f"O{f}{r}")

        else:

            if f == floors:
                listBuilding.append(f"L{f}{r}")
            else:
                listBuilding.append(f"A{f}{r}")

listBuilding.reverse()

for f in range(1,floors+1):
    list1 = listBuilding[0:rooms]
    list1.reverse()
    print(' '.join(list1))
    del listBuilding[0:rooms]
