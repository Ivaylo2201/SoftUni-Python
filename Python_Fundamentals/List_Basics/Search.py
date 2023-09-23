n = int(input())
word = input()
wordsList = []

for _ in range(n):
    words = input()
    wordsList.append(words)

includedList = [wordsList[x] for x in range(len(wordsList)) if word in wordsList[x]]
print(wordsList)
print(includedList)
