grades_dict = {}
n = int(input())
for _ in range(n):
    name = input()
    grade = float(input())

    if name not in grades_dict:
        grades_dict[name] = []
    grades_dict[name].append(grade)

for key, value in grades_dict.items():
    avg = sum(value)/len(value)
    if avg >= 4.5:
        print(f"{key} -> {format(avg, '.2f')}")
