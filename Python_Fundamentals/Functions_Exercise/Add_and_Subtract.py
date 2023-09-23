def sum_numbers(number1, number2):
    return number1 + number2

def subtract(number1, number2, number3):
    return sum_numbers(number1, number2) - number3

def add_and_subtract(number1, number2, number3):
    print(subtract(number1, number2, number3))

num1 = int(input())
num2 = int(input())
num3 = int(input())

add_and_subtract(num1, num2, num3)
