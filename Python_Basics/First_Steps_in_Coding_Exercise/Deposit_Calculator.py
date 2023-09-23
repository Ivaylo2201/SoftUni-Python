deposit = float(input())
depositPeriod = int(input())
flatPercent = float(input())
percent = flatPercent / 100

total = float(deposit + depositPeriod * ((deposit * percent) / 12))

print(total)
