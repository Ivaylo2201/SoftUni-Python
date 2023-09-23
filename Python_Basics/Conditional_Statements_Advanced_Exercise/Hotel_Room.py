month = input()
nightsCount = int(input())
studioPrice = 0
apartmentPrice = 0
if month == 'May' or month == 'October':
    studioPrice = 50
    apartmentPrice = 65
    if 7 < nightsCount <= 14:
        studioPrice = studioPrice - 0.05 * studioPrice
    elif nightsCount > 14:
        studioPrice = studioPrice - 0.30 * studioPrice
        apartmentPrice = apartmentPrice - 0.10 * apartmentPrice
elif month == 'June' or month == 'September':
    studioPrice = 75.20
    apartmentPrice = 68.70
    if nightsCount > 14:
        studioPrice = studioPrice - 0.20 * studioPrice
        apartmentPrice = apartmentPrice - 0.10 * apartmentPrice
elif month == 'July' or month == 'August':
    studioPrice = 76
    apartmentPrice = 77
    if nightsCount > 14:
        apartmentPrice = apartmentPrice - 0.10 * apartmentPrice
print(f"Apartment: {format(apartmentPrice*nightsCount,'.2f')} lv.")
print(f"Studio: {format(studioPrice*nightsCount,'.2f')} lv.")
