text = input()
textDict = {}

for char in text:
    if char != " ":
        if char not in textDict:
            textDict[char] = 1
        else:
            textDict[char] += 1

for key, value in textDict.items():
    print(f"{key} -> {value}")
