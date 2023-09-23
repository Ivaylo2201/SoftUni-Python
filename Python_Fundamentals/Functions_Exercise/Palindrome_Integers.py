nums = [x for x in input().split(", ")]
palindrome = [x for x in nums if x == x[::-1]]

for x in nums:
    if x == x[::-1]:
        print("True")
    else:
        print("False")
