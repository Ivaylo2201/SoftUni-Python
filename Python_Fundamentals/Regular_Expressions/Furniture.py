import re
pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>[\d\.]+)!(?P<quantity>[\d]+)"
item_info_list = []
total = 0

while True:
    info = input()
    if info == 'Purchase':
        break

    matches = re.finditer(pattern, info)

    for item in matches:
        item_dict = item.groupdict()
        item_info_list.append([item_dict['name'], float(item_dict['price']), int(item_dict['quantity'])])
        total += float(item_dict['price']) * int(item_dict['quantity'])

print("Bought furniture:")
for item in item_info_list:
    print(item[0])
print(f"Total money spend: {format(total, '.2f')}")
