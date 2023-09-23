parking_lot = {}
n = int(input())
for i in range(n):
    command = input().split()
    if command[0] == 'register':
        username = command[1]
        license_plate = command[2]
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    elif command[0] == 'unregister':
        username = command[1]
        if username in parking_lot:
            del parking_lot[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for key, value in parking_lot.items():
    print(f"{key} => {value}")

