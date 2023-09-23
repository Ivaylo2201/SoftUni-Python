stepsList = []
while True:
    steps = input()

    if steps == "Going home":
        stepsToHome = int(input())
        stepsList.append(stepsToHome)
        if sum(stepsList) > 10000:
            print("Goal reached! Good job!")
            print(f"{sum(stepsList) - 10000} steps over the goal!")
            quit()
        else:
            print(f"{abs(sum(stepsList) - 10000)} more steps to reach goal.")
            quit()

    stepsList.append(int(steps))

    if sum(stepsList) > 10000:
        print("Goal reached! Good job!")
        print(f"{sum(stepsList) - 10000} steps over the goal!")
        quit()
