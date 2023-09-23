wagons = int(input())
train = [0] * wagons

while True:
    command_string = input().split()
    if command_string[0] == 'End':
        break
    command = command_string[0]

    if command == 'add':
        people = int(command_string[1])
        train[-1] += people

    elif command == 'insert':
        index = int(command_string[1])
        people = int(command_string[2])
        train[index] += people

    elif command == 'leave':
        index = int(command_string[1])
        people = int(command_string[2])
        train[index] -= people

print(train)

