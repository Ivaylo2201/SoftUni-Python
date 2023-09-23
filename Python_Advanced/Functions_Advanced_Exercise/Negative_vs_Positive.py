def func(*args):
    sum_pos = 0
    sum_neg = 0

    for num in args:
        if num > 0:
            sum_pos += num
        else:
            sum_neg += num

    print(sum_neg)
    print(sum_pos)

    if abs(sum_neg) > sum_pos:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


func(*[int(x) for x in input().split()])
