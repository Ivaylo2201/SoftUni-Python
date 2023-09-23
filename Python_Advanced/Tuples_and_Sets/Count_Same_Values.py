numbers = tuple([float(x) for x in input().split()])
occur = {}

for num in numbers:
    if num not in occur:
        occur[num] = 1
    else:
        occur[num] += 1

for num, value in occur.items():
    print(f"{num} - {value} times")
