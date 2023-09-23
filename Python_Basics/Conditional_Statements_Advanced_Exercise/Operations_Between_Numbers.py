num1 = float(input())
num2 = float(input())
operator = input()

result = 0
evenOrOdd = ''
if operator == '+':
    result = num1 + num2
    if result % 2 == 0:
        evenOrOdd = 'even'
    else:
        evenOrOdd = 'odd'
    print(f"{int(num1)} {operator} {int(num2)} = {int(result)} - {evenOrOdd}")

elif operator == '-':
    result = num1 - num2
    if result % 2 == 0:
        evenOrOdd = 'even'
    else:
        evenOrOdd = 'odd'
    print(f"{int(num1)} {operator} {int(num2)} = {int(result)} - {evenOrOdd}")

elif operator == '*':
    result = num1 * num2
    if result % 2 == 0:
        evenOrOdd = 'even'
    else:
        evenOrOdd = 'odd'
    print(f"{int(num1)} {operator} {int(num2)} = {int(result)} - {evenOrOdd}")

elif operator == '/':
    try:
        result = num1 / num2
        print(f"{int(num1)} {operator} {int(num2)} = {format(result, '.2f')}")
    except ZeroDivisionError:
        print(f"Cannot divide {int(num1)} by zero")


elif operator == '%':
    try:
        result = num1 % num2
        print(f"{int(num1)} {operator} {int(num2)} = {int(result)}")
    except ZeroDivisionError:
        print(f"Cannot divide {int(num1)} by zero")
