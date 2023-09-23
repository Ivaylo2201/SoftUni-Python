actorName = input()
points = float(input())
judgesCount = int(input())

for i in range(judgesCount):
    judgeName = input()
    judgePoints = float(input())
    points += (len(judgeName) * judgePoints) / 2

    if points >= 1250.5:
        print(f"Congratulations, {actorName} got a nominee for leading role with {format(points, '.1f')}!")
        quit()

if points < 1250.5:
    print(f"Sorry, {actorName} you need {format(1250.5 - points, '.1f')} more!")
