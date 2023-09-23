def onlyEvens():
    nums = [int(x) for x in input().split()]
    evens = [x for x in nums if x % 2 == 0]
    return evens


print(onlyEvens())
