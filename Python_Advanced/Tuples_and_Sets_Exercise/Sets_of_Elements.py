n, m = [int(x) for x in input().split()]

set_n = set()
set_m = set()

for _ in range(n):
    num = int(input())
    set_n.add(num)

for _ in range(m):
    num = int(input())
    set_m.add(num)

print(*(set_n.intersection(set_m)), sep='\n')
