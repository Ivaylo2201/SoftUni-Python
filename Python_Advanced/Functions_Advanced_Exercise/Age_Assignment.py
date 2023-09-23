def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            result.append(f"{name} is {kwargs[first_letter]} years old.")

    return '\n'.join(sorted(result))
