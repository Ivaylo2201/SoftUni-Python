n = int(input())
salary = float(input())

for i in range(n):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50
    else:
        salary -= 0

    if salary <= 0:
        print("You have lost your salary.")
        quit()

print(int(salary))
