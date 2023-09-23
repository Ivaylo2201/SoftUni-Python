text = input()
occurrences = {}

for ch in text:
    if ch not in occurrences:
        occurrences[ch] = 0
    occurrences[ch] += 1

occurrences = sorted(occurrences.items())
for pair in occurrences:
    print(f'{pair[0]}: {pair[1]} time/s')
