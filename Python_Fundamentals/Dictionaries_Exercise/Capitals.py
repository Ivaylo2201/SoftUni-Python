countries = input().split(', ')
cities = input().split(', ')
city_country_dict = {key:value for (key,value) in zip(countries, cities)}

for key, value in city_country_dict.items():
    print(f"{key} -> {value}")
