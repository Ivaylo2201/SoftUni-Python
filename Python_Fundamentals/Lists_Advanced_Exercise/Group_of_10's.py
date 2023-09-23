from math import ceil

nums = [int(x) for x in input().split(", ")]

low = 1
high = 10
total_groups = ceil(max(nums)/10)+1

for i in range(1, total_groups):
    sorted_nums = [x for x in nums if low <= x <= high]
    print(f"Group of {10*i}'s: {sorted_nums}")

    low += 10
    high += 10


tens = [x for x in nums if 0 < x <= 10]
twenties = [x for x in nums if 10 < x <= 20]
thirties = [x for x in nums if 20 < x <= 30]
forties = [x for x in nums if 30 < x <= 40]
fifties = [x for x in nums if 40 < x <= 50]

if tens:
    print(f"Group of 10's: {tens}")
if twenties:
    print(f"Group of 20's: {twenties}")
if thirties:
    print(f"Group of 30's: {thirties}")
if forties:
    print(f"Group of 40's: {forties}")
if fifties:
    print(f"Group of 50's: {fifties}")
