nums = [int(x) for x in input().split(', ')]

positives = [x for x in nums if x >= 0]
negatives = [x for x in nums if x < 0]
evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x % 2 != 0]

positives = [str(x) for x in positives]
negatives = [str(x) for x in negatives]
evens = [str(x) for x in evens]
odds = [str(x) for x in odds]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(evens)}")
print(f"Odd: {', '.join(odds)}")
