n = int(input())
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        quit()
    else:
        continue
print("All numbers are even.")
