exam_dict = {}
submissions_dict = {}
while True:
    data = input().split('-')
    if data[0] == 'exam finished':
        break
    elif data[1] == 'banned':
        username = data[0]
        for key, value in exam_dict.items():
            for key1 in value:
                if key1 == username:
                    del exam_dict[key][key1]
                    break
            continue
    else:
        username = data[0]
        language = data[1]
        points = int(data[2])

        if language not in exam_dict:
            exam_dict[language] = {}
        if language not in submissions_dict:
            submissions_dict[language] = 1
        else:
            submissions_dict[language] += 1

        if username in exam_dict[language]:
            if exam_dict[language][username] < points:
                exam_dict[language][username] = points
        else:
            exam_dict[language][username] = points

print("Results:")
for key, value in exam_dict.items():
    for key1, value1 in value.items():
        print(f"{key1} | {value1}")

print("Submissions:")
for key, value in submissions_dict.items():
    print(f"{key} - {value}")
