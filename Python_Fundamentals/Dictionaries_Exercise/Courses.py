courses = {}
while True:
    data = input().split(" : ")
    if data[0] == 'end':
        break
    else:
        if data[0] not in courses:
            courses[data[0]] = []
            courses[data[0]].append(data[1])
        else:
            courses[data[0]].append(data[1])

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for person in value:
        print(f"-- {person}")
