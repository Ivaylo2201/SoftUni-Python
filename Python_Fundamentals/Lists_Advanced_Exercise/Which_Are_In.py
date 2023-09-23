words1 = input().split(", ")
words2 = input().split(", ")
subsList = []

for string in words1:
    for word in words2:
        if string in word and string not in subsList:
            subsList.append(string)

print(subsList)
