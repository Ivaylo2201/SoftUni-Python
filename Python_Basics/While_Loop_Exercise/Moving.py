homeWidth = int(input())
homeLength = int(input())
homeHeight = int(input())
homeSize = homeWidth * homeLength * homeHeight

while True:
    boxesCount = input()

    if boxesCount != 'Done':
        boxesCount = int(boxesCount)
        homeSize -= boxesCount

        if homeSize <= 0:
            print(f"No more free space! You need {abs(homeSize)} Cubic meters more.")
            quit()

    else:
        print(f"{homeSize} Cubic meters left.")
        quit()
