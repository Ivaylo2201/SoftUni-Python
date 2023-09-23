ToDoList = [' '] * 10
while True:
    command_args = input().split('-')
    if command_args[0] == 'End':
        break
    ToDoList[int(command_args[0])] = command_args[1]

ToDoListPrint = [x for x in ToDoList if x != ' ']
print(ToDoListPrint)
