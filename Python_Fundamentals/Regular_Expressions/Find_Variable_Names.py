import re
pattern = r"\b_[A-Za-z0-9]+\b"
text = input()
final_word = ''
final_result = []

result = re.findall(pattern, text)

for word in result:
    final_word = word.replace("_", '')
    final_result.append(final_word)

print(','.join(final_result))
