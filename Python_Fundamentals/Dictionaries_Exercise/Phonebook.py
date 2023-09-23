phonebook = {}
n = 0
while True:
    entry = input()
    if '-' not in entry:
        n = int(entry)
        break
    else:
        entry = entry.split("-")
        if entry[0] not in phonebook:
            phonebook[entry[0]] = entry[1]

for _ in range(n):
    contact = input()
    if contact in phonebook:
            print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
