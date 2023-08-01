# Input the number of the day
day = int(input("Enter the number of the day: "))

# Calculate the date of the day in 2023
year = 2023
month = 1
if day <= 31:
    day = day
elif day <= 59:
    month = 2
    day = day - 31
elif day <= 90:
    month = 3
    day = day - 59
elif day <= 120:
    month = 4
    day = day - 90
elif day <= 151:
    month = 5
    day = day - 120
elif day <= 181:
    month = 6
    day = day - 151
elif day <= 212:
    month = 7
    day = day - 181
elif day <= 243:
    month = 8
    day = day - 212
elif day <= 273:
    month = 9
    day = day - 243
elif day <= 304:
    month = 10
    day = day - 273
elif day <= 334:
    month = 11
    day = day - 304
else:
    month = 12
    day = day - 334

# Output the date in yyyy/mm/dd format
print(str(year) + "/" + str(month).zfill(2) + "/" + str(day).zfill(2))