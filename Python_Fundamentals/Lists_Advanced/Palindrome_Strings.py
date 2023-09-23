words = input().split()
palindrome = input()
palindromesList = []

for word in words:
    if word == word[::-1]:
        palindromesList.append(word)

occurrences = 0
for pal in palindromesList:
    if palindrome == pal:
        occurrences += 1

print(palindromesList)
print(f"Found palindrome {occurrences} times")
