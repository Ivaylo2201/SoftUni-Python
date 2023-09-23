import re
pattern = r"\d+"

result = []

while True:
    text = input()
    if not text:
        break

    matches = re.findall(pattern, text)
    result.extend(matches)

print(' '.join(result))
