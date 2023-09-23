names_count = int(input())
names = []

for _ in range(names_count):
    name = input()
    names.append(name)

names = set(names)
for name in names:
    print(name)
