def absNums(x):
    return [abs(i) for i in numsF]


numsF = [float(x) for x in input().split()]
print(absNums(numsF))
