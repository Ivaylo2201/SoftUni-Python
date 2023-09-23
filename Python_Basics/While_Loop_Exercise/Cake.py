cakeWidth = int(input())
cakeHeight = int(input())
cakePieces = cakeHeight * cakeWidth

while True:
    cakePiecesTaken = input()

    if cakePiecesTaken != 'STOP':
        cakePiecesTaken = int(cakePiecesTaken)
        cakePieces -= cakePiecesTaken

        if cakePieces <= 0:
            print(f"No more cake left! You need {abs(cakePieces)} pieces more.")
            quit()

    else:
        print(f"{cakePieces} pieces are left.")
        quit()
