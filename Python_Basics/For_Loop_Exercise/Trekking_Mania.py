groupCount = int(input())
totalPeople = []
groupMusala = []
groupMontblanc = []
groupKilimanjaro = []
groupK2 = []
groupEverest = []

for i in range(groupCount):
    groupPeople = int(input())
    totalPeople.append(groupPeople)

    if groupPeople <= 5:
        groupMusala.append(groupPeople)
    elif 6 <= groupPeople <= 12:
        groupMontblanc.append(groupPeople)
    elif 13 <= groupPeople <= 25:
        groupKilimanjaro.append(groupPeople)
    elif 26 <= groupPeople <= 40:
        groupK2.append(groupPeople)
    elif groupPeople >= 41:
        groupEverest.append(groupPeople)

totalPeopleSum = sum(totalPeople)
groupMusalaSum = sum(groupMusala)
groupMontblancSum = sum(groupMontblanc)
groupKilimanjaroSum = sum(groupKilimanjaro)
groupK2Sum = sum(groupK2)
groupEverestSum = sum(groupEverest)

musalaPercentage = (groupMusalaSum / totalPeopleSum) * 100
montblancPercentage = (groupMontblancSum / totalPeopleSum) * 100
kilimanjaroPercentage = (groupKilimanjaroSum / totalPeopleSum) * 100
k2Percentage = (groupK2Sum / totalPeopleSum) * 100
everestPercentage = (groupEverestSum / totalPeopleSum) * 100

print(f"{format(musalaPercentage,'.2f')}%")
print(f"{format(montblancPercentage,'.2f')}%")
print(f"{format(kilimanjaroPercentage,'.2f')}%")
print(f"{format(k2Percentage,'.2f')}%")
print(f"{format(everestPercentage,'.2f')}%")
