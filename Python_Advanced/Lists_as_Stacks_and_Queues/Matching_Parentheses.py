expression = input()
open_par = []
closing_par = []

for i in range(len(expression)):
    if expression[i] == '(':
        open_par.append(i)
    elif expression[i] == ')':
        start = int(open_par.pop())
        end = i
        print(expression[start:end+1])
