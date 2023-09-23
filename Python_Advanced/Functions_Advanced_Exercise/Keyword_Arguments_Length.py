def kwargs_length(**kwargs):
    counter = 0
    for value in kwargs.values():
        counter += 1

    return counter
