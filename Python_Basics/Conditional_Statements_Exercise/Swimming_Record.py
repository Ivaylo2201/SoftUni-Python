recordSec = float(input())
lengthMeters = float(input())
timeFor1meter = float(input())
time = lengthMeters * timeFor1meter
slow = (lengthMeters // 15) * 12.5
timeTotal = time + slow
if timeTotal >= recordSec:
    print(f"No, he failed! He was {format(timeTotal-recordSec, '.2f')} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {format(timeTotal, '.2f')} seconds.")
