tournaments = int(input())
points = int(input())
pointsWon = []
tournamentsWon = 0

for i in range(tournaments):
    tournamentStage = input()

    if tournamentStage == 'W':
        points += 2000
        pointsWon.append(2000)
        tournamentsWon += 1
    elif tournamentStage == 'F':
        points += 1200
        pointsWon.append(1200)
    elif tournamentStage == 'SF':
        points += 720
        pointsWon.append(720)

averagePoints = sum(pointsWon) / tournaments
victoryPercentage = (tournamentsWon / tournaments) * 100

print(f"Final points: {points}")
print(f"Average points: {int(averagePoints)}")
print(f"{format(victoryPercentage,'.2f')}%")
