version = [int(x) for x in input().split('.')]

if version[2] <= 8:
    version[2] += 1
else:
    version[2] = 0
    if version[1] <= 8:
        version[1] += 1
    else:
        version[1] = 0
        version[0] += 1

version = [str(x) for x in version]
print('.'.join(version))
