def squares(n: int):
    for i in range(1, n + 1):
        yield i ** 2


for t in squares(5):
    print(t)
