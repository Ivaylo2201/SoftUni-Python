dictItems = {}
pos = ''
for i in range(1, 100, 1):
    if i % 2 != 0:
        key = input()
        if key == 'stop':
            break
        else:
            if key not in dictItems:
                dictItems[key] = 0
            pos += key
    else:
        value = input()
        if value == 'stop':
            break
        else:
            dictItems[pos] += int(value)
            pos = ""

for key, value in dictItems.items():
    print(f"{key} -> {value}")
