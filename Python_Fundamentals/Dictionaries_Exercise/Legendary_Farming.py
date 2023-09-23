items = {}
junk = {}
legItem = None
while True:
    item_quantity = input().split()
    for i in range(0, len(item_quantity), 2):
        if item_quantity[i + 1].lower() in ["shards", "fragments", "motes"]:
            if item_quantity[i + 1].lower() not in items:
                items[item_quantity[i + 1].lower()] = int(item_quantity[i])
            else:
                items[item_quantity[i + 1].lower()] += int(item_quantity[i])

            for key, value in items.items():
                if value >= 250:
                    if key == 'shards':
                        legItem = "xd"
                        items[key] -= 250
                    elif key == 'fragments':
                        legItem = 'xd'
                        items[key] -= 250
                    elif key == 'motes':
                        legItem = 'xd'
                        items[key] -= 250

                    if items.get("shards") is None:
                        items["shards"] = 0
                    if items.get("fragments") is None:
                        items["fragments"] = 0
                    if items.get("motes") is None:
                        items["motes"] = 0

                    print(f"{legItem} obtained!")
                    print(f"shards: {items['shards']}")
                    print(f"fragments: {items['fragments']}")
                    print(f"motes: {items['motes']}")
                    for key_junk, value_junk in junk.items():
                        print(f"{key_junk}: {value_junk}")

                    quit()

        else:
            if item_quantity[i + 1].lower() not in junk:
                junk[item_quantity[i + 1].lower()] = int(item_quantity[i])
            else:
                junk[item_quantity[i + 1].lower()] += int(item_quantity[i])
