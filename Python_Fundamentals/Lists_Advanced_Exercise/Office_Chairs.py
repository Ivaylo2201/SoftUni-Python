rooms = int(input())
remainingChairs = 0

for i in range(1, rooms + 1):
    room = input().split()
    chairs = len(room[0])
    visitors = int(room[1])

    if visitors > chairs:
        print(f"{visitors - chairs} more chairs needed in room {i}")
        remainingChairs -= visitors - chairs
    else:
        remainingChairs += chairs - visitors

if remainingChairs > 0:
    print(f"Game On, {remainingChairs} free chairs left")
