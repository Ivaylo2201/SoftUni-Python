employees = [int(x) for x in input().split()]
happinessFactor = int(input())

multipliedHappiness = [x*happinessFactor for x in employees]
average = sum(multipliedHappiness) / len(employees)

happyPeople = 0
for i in multipliedHappiness:
    if i >= average:
        happyPeople += 1

if happyPeople >= len(employees) // 2:
    print(f"Score: {happyPeople}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {happyPeople}/{len(employees)}. Employees are not happy!")
