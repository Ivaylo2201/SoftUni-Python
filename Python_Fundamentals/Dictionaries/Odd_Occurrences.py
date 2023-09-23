words = input().split()
wordDict = {}

for word in words:
    word = word.lower()
    if word not in wordDict:
        wordDict[word] = 1
    else:
        wordDict[word] += 1

wordDictOdd = {key: value for (key, value) in wordDict.items() if value % 2 != 0}
print(' '.join(wordDictOdd.keys()))
