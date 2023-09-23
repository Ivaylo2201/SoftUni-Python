message = input().split()
finalOutputString = ""
finalOutputList = []

for word in message:
    finalOutputList.clear()
    charCodeList = []
    remainingChars = []
    for i in word:
        if i.isdigit():
            charCodeList.append(i)
        else:
            remainingChars.append(i)

    charCode = chr(int(''.join(charCodeList)))

    finalOutputList.append(charCode)
    for x in remainingChars:
        finalOutputList.append(x)
    secChar = finalOutputList[1]
    lastChar = finalOutputList[-1]

    finalOutputList[1] = lastChar
    finalOutputList[-1] = secChar

    finalOutputString += ''.join(finalOutputList)
    finalOutputString += ' '

print(''.join(finalOutputString))
