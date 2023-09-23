def fact(num1, num2):
    fact_num1 = 1
    for i in range(1, num1+1):
        fact_num1 *= i

    fact_num2 = 1
    for i in range(1, num2+1):
        fact_num2 *= i

    result = format(fact_num1 / fact_num2, '.2f')
    return result

n1 = int(input())
n2 = int(input())
print(fact(n1,n2))
