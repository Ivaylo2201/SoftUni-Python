def even_parameters(function):
    def wrapper(*args):
        numbers = all([isinstance(x, int) for x in args])
        if not numbers:
            return "Please use only even numbers!"

        even_numbers = all([True if x % 2 == 0 else False for x in args])
        if even_numbers:
            return function(*args)
        else:
            return "Please use only even numbers!"

    return wrapper
