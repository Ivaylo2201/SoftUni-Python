beginning = int(input())
end = int(input())
magicNum = int(input())

combinationPossible = 0
for i1 in range(beginning, end + 1):
    for j1 in range(beginning, end + 1):
        combinationPossible += 1

combination = 0
for i in range(beginning, end + 1):
    for j in range(beginning, end + 1):
        combination += 1

        result = i + j

        if result == magicNum:
            print(f"Combination N:{combination} ({i} + {j} = {magicNum})")
            quit()

if result != magicNum:
    print(f"{combinationPossible} combinations - neither equals {magicNum}")
    quit()
