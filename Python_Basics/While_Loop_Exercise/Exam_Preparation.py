listGrades = []
listTasks = []
listFails = []
failures = int(input())
tasks = 0

while True:
    taskName = input()

    if taskName != "Enough":
        tasks += 1
        listTasks.append(taskName)

        grade = int(input())
        if grade <= 4:
            listFails.append(grade)

        listGrades.append(grade)

        if len(listFails) >= failures:
            print(f"You need a break, {len(listFails)} poor grades.")
            quit()

    else:
        average = sum(listGrades) / tasks
        lastProblem = listTasks[-1]
        print(f"Average score: {format(average, '.2f')}")
        print(f"Number of problems: {tasks}")
        print(f"Last problem: {lastProblem}")
        quit()
