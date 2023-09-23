def perfect_Nums(num):
    num_divisors = []
    result = None

    i = 1
    while i < num:
        if num % i == 0:
            num_divisors.append(i)
        i += 1

    if sum(num_divisors) == num:
        result = "We have a perfect number!"
    else:
        result = "It's not so perfect."

    return result

n = int(input())
print(perfect_Nums(n))
