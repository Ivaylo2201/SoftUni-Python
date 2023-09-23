n_students = int(input())
students = {}
for _ in range(n_students):
    data = input().split()

    name = data[0]
    grade = float(data[1])

    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for key, value in students.items():
    avg = format(sum(students[key]) / len(students[key]), '.2f')
    grades = ' '.join([format(x, '.2f') for x in students[key]])

    print(f'{key} -> {grades} (avg: {avg})')
