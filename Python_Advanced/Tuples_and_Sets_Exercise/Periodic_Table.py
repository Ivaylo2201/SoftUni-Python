n = int(input())
unique_chemicals = set()

for _ in range(n):
    chemicals_compounds = input().split()

    for chemical in chemicals_compounds:
        unique_chemicals.add(chemical)

print(*unique_chemicals, sep='\n')
