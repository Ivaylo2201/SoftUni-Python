def Calc(act, num1, num2):
    if act == "multiply":
        return num1 * num2
    elif act == "divide":
        return int(num1 / num2)
    elif act == "add":
        return num1 + num2
    elif act == "subtract":
        return num1 - num2


action = input()
number1 = int(input())
number2 = int(input())

print(Calc(action, number1, number2))
