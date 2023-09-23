size = int(input())

commands = input().split()
matrix = [input().split() for _ in range(size)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

miner_location = []
coal_mined = 0

for idx, row in enumerate(matrix):
    if 's' in row:
        miner_location = [idx, row.index('s')]
        break

for command in commands:
    if 0 <= miner_location[0] + directions[command][0] < size and 0 <= miner_location[1] + directions[command][1] < size:

        miner_location = [miner_location[0] + directions[command][0], miner_location[1] + directions[command][1]]

        if matrix[miner_location[0]][miner_location[1]] == 'c':
            coal_mined += 1
            matrix[miner_location[0]][miner_location[1]] = '*'

        elif matrix[miner_location[0]][miner_location[1]] == 'e':
            print(f"Game over! ({miner_location[0]}, {miner_location[1]})")
            exit()
    else:
        continue

current_amount_of_coal = 0
for row in matrix:
    if 'c' in row:
        current_amount_of_coal += 1

if not current_amount_of_coal:
    print(f"You collected all coal! ({miner_location[0]}, {miner_location[1]})")
else:
    print(f"{current_amount_of_coal} pieces of coal left. ({miner_location[0]}, {miner_location[1]})")
