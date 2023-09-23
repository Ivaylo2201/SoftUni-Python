numsString = input().split()
string = list(input())
strLen = len(string)
result = []

for x in numsString:
    sumDigits = sum([int(i) for i in x])
    if sumDigits < strLen:
        result.append(string[sumDigits])
        string.pop(sumDigits)
    else:
        result.append(string[sumDigits - strLen])
        string.pop(sumDigits - strLen)

print(''.join(result))
