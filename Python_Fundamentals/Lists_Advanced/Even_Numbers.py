nums = [int(x) for x in input().split(', ')]
evenIndices = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        evenIndices.append(i)

print(evenIndices)
