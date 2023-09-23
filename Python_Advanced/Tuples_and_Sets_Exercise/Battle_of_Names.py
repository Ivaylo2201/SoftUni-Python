n = int(input())

set_even = set()
set_odd = set()

for i in range(1, n+1):
    name_sum = 0
    name = input()

    for ch in name:
        name_sum += ord(ch)

    result = name_sum // i

    if result % 2 == 0:
        set_even.add(result)
    else:
        set_odd.add(result)

if sum(set_even) == sum(set_odd):
    print(', '.join([str(x) for x in set_even.union(set_odd)]))
elif sum(set_even) < sum(set_odd):
    print(', '.join([str(x) for x in set_odd.difference(set_even)]))
elif sum(set_even) > sum(set_odd):
    print(', '.join([str(x) for x in set_odd.symmetric_difference(set_even)]))
