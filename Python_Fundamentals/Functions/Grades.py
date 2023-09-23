def gradeS(x):
    if 2 <= x <= 2.99:
        return "Fail"
    elif 3 <= x <= 3.49:
        return "Poor"
    elif 3.50 <= x <= 4.49:
        return "Good"
    elif 4.50 <= x <= 5.49:
        return "Very Good"
    elif 5.50 <= x <= 6:
        return "Excellent"

grade = float(input())
print(gradeS(grade))
