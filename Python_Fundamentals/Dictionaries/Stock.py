elements = input().split()
dictionary = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = int(elements[i+1])
    dictionary[key] = value

searched_products = input().split()
for searched_product in searched_products:
    if searched_product in dictionary.keys():
        print(f"We have {dictionary[searched_product]} of {searched_product} left")
    else:
        print(f"Sorry, we don't have {searched_product}")
