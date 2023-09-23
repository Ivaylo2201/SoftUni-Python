n = int(input())
numsUnder200 = []
numsBetween200and399 = []
numsBetween400and599 = []
numsBetween600and799 = []
numsOver800 = []

for i in range(n):
    num = int(input())
    if num < 200:
        numsUnder200.append(num)
    elif 200 <= num <= 399:
        numsBetween200and399.append(num)
    elif 400 <= num <= 599:
        numsBetween400and599.append(num)
    elif 600 <= num <= 799:
        numsBetween600and799.append(num)
    elif num >= 800:
        numsOver800.append(num)

numsUnder200Count = len(numsUnder200)
numsBetween200and399Count = len(numsBetween200and399)
numsBetween400and599Count = len(numsBetween400and599)
numsBetween600and799Count = len(numsBetween600and799)
numsOver800Count = len(numsOver800)

p1 = (numsUnder200Count / n) * 100
p2 = (numsBetween200and399Count / n) * 100
p3 = (numsBetween400and599Count / n) * 100
p4 = (numsBetween600and799Count / n) * 100
p5 = (numsOver800Count / n) * 100

print(f"{format(p1,'.2f')}%")
print(f"{format(p2,'.2f')}%")
print(f"{format(p3,'.2f')}%")
print(f"{format(p4,'.2f')}%")
print(f"{format(p5,'.2f')}%")
