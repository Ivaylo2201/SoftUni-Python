n = int(input())
listPositives = []
listNegatives = []

for _ in range(n):
    num = int(input())
    if num >= 0:
        listPositives.append(num)
    else:
        listNegatives.append(num)

print(listPositives)
print(listNegatives)
print(f"Count of positives: {len(listPositives)}")
print(f"Sum of negatives: {sum(listNegatives)}")
