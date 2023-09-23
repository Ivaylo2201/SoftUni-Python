number = float(input())
numberType = ""
absoluteValueType = ""

if number == 0:
    print("zero")
elif number > 0:
    numberType = "positive"
else:
    numberType = "negative"

if abs(number) < 1 and abs(number) != 0:
    absoluteValueType = "small"
elif abs(number) > 1000000:
    absoluteValueType = "large"

print(f"{absoluteValueType} {numberType}")
