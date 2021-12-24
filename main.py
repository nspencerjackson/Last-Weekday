from datetime import date
from checkDay import *

newYear = False

# Gets the date
print("What is the day?:")
day = input()
print("What is the month?:")
m = input()
print("What is the year?:")
y = input()

# makes x today's date
x = date(int(y), int(m), int(day))

# Checks if today is the first of the month
if x.day == 1:
    # Checks if it is the first day of a new year (make this a function)
    if x.month == 1:
        lastYearDate = checkYear(int(m), int(day), y)
        newYear = True
    # Else not the first month
    else:
        lastMonth = x.month - 1
        prev = lastDay(lastMonth, y)
# else not the first day of the month
elif x.day > 1:
    # If it is January
    if x.month == 1:
        newYear = True
        lastYearDate = checkYear(int(m), int(day), y)
    # else any other month
    else:
        # if it is a Monday
        if x.weekday() == 0:
            lastMonth = x.month
            prev = prevDay(x.month, x.day, x.year)
        # else-if any other day upto Saturday
        elif x.weekday() <= 5:
            prev = x.day - 1
            lastMonth = x.month
        # else it is a Sunday
        elif x.weekday() == 6:
            prev = x.day - 2
            lastMonth = x.month

if newYear:
    lastMonth = lastYearDate.month
    y = lastYearDate.year
    prev = lastYearDate.day

s = date(int(y), int(lastMonth), int(prev))
print("The last date of the week is:", s)
