timeFirst = int(input())
timeSecond = int(input())
timeThird = int(input())

timeAll = (timeFirst + timeSecond + timeThird)
timeMin = timeAll // 60
timeSec = timeAll % 60

if timeSec < 10:
    print(f'{timeMin}:0{timeSec}')
else:
    print(f'{timeMin}:{timeSec}')
