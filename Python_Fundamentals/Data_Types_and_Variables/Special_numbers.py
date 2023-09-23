def sumDigit(num):
    digitSum = 0
    for digit in str(num):
        digitSum += int(digit)
    return digitSum


n = int(input())
for i in range(1, n + 1):
    if sumDigit(i) == 5 or sumDigit(i) == 7 or sumDigit(i) == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
