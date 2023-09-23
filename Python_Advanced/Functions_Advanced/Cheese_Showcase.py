def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x))
    for cheese_name, quantity in sorted_cheeses:
        result += cheese_name + "\n"
        reversed_quantities = sorted(quantity, reverse=True)
        result += "\n".join(str(el) for el in reversed_quantities)
        result += "\n"

    return result
