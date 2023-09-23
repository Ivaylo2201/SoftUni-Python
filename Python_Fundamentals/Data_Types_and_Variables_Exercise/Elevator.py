import math

people = int(input())
elevatorCapacity = int(input())

fullCourses = math.ceil(people/elevatorCapacity)
print(fullCourses)
