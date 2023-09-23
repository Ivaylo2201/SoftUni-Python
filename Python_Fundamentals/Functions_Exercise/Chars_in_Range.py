def charsBetween(beginning, end):
    result = []
    str1_id = ord(beginning)
    str2_id = ord(end)
    for i in range(str1_id +1, str2_id):
        result.append(chr(i))
    return ' '.join(result)

str1 = input()
str2 = input()
print(charsBetween(str1, str2))
