numString = input().split(", ")
numsInt = [int(x) for x in numString]

zeros = [x for x in numsInt if x == 0]
nums = [x for x in numsInt if x != 0]

nums.extend(zeros)
print(nums)
