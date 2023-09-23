import math

shape = input()
area = 0
if shape == 'square':
    side = float(input())
    area = math.pow(side, 2)
    print(area)
elif shape == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
    print(area)
elif shape == 'circle':
    radius = float(input())
    area = math.pi * (math.pow(radius, 2))
    print(area)
elif shape == 'triangle':
    side1 = float(input())
    side2 = float(input())
    area = (side1 * side2)/2
    print(area)
