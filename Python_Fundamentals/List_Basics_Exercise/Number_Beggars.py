numbers = input().split(", ")
countBeggars = int(input())

beggarsList = [0] * countBeggars

for idx in range(len(numbers)):
    beggarIdx = idx % countBeggars
    num = int(numbers[idx])
    beggarsList[beggarIdx] += num

print(beggarsList)
