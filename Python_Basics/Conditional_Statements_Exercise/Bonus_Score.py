startingPoints = int(input())
bonusPoints = 0

num_str = repr(startingPoints)
lastDigit_str = num_str[-1]
lastDigit = int(lastDigit_str)

if startingPoints <= 100:
    bonusPoints = 5
elif 100 < startingPoints < 1000:
    bonusPoints = 0.20 * startingPoints
elif startingPoints >= 1000:
    bonusPoints = 0.10 * startingPoints

if startingPoints % 2 == 0:
    bonusPoints += 1
if lastDigit == 5:
    bonusPoints += 2

print(bonusPoints)
print(bonusPoints + startingPoints)
