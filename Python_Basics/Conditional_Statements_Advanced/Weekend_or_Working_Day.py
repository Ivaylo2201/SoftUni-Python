day = input()
output = ''
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    output = 'Working day'
elif day == 'Saturday' or day == 'Sunday':
    output = 'Weekend'
else:
    output = 'Error'
print(output)
