def roundNums():
    return [round(x) for x in numsInt]


nums = input().split()
numsInt = [float(x) for x in nums]

print(roundNums())
