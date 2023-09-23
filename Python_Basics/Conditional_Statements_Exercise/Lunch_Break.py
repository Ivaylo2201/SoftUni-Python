import math
movieName = input()
episodeLength = int(input())
breakLength = int(input())
lunch = breakLength / 8
rest = breakLength / 4
remainingTime = breakLength - lunch - rest
if remainingTime >= episodeLength:
    print(f"You have enough time to watch {movieName} and left with {math.ceil(remainingTime - episodeLength)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movieName}, you need {math.ceil(episodeLength - remainingTime)} more minutes.")
