def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == 'even':
            kwargs[key] = [num for num in value if num % 2 == 0]
        elif key == 'odd':
            kwargs[key] = [num for num in value if num % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda x: len(x[1]), reverse=True))
