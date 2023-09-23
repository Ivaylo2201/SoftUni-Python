length = int(input())
width = int(input())
height = int(input())
flatPercent = float(input())
percent = flatPercent / 100
v = (length * width * height)/1000
vFinal = v - v * percent
print(vFinal)
