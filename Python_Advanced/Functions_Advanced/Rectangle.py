def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    result = ""

    def area():
        return length*width

    def perimeter():
        return 2*length+2*width

    result += f"Rectangle area: {area()}" + "\n"
    result += f"Rectangle perimeter: {perimeter()}"

    return result
