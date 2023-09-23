def type_check(data_type):
    def decorator(function):
        def wrapper(*args):
            return function(args) if isinstance(args, data_type) else "Bad Type"
        return wrapper
    return decorator
