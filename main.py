from datetime import date
from checkDay import *

# Gets the date
print("What is the day?:")
day = input()
print("What is the month?:")
m = input()
print("What is the year?:")
y = input()

# makes x today's date
x = date(int(y), int(m), int(day))
print("the weekday is: ", x.weekday())
print(x.day)

# Checks if today is the first of the month
if x.day == 1:
    # Checks if it is the first day of a new year (make this a function)
    if x.month == 1:
        lastMonth = 12
        prev = lastDay(lastMonth)
        y = str(int(y) - 1)
    else:
        lastMonth = x.month - 1
        prev = lastDay(lastMonth)
elif x.day > 1:
    if x.weekday() == 0:
        lastMonth = x.month
        prev = prevDay(x.month, x.day)
    elif x.weekday() <= 5:
        print("now")
        prev = x.day - 1
        lastMonth = x.month
        print("pot - ", lastMonth)
    elif x.weekday() == 6:
        prev = x.day - 2
        lastMonth = x.month
        print("ato - ", lastMonth)

s = date(int(y), int(lastMonth), int(prev))
print("The last date of the week is:", s)
