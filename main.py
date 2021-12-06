from datetime import date
from checkDay import *

print("What is the day?:")
day = input()
print("What is the month?:")
m = input()
pring("What is the year?:")
y = input()

x = date(int(y), int(m), int(day))
print(x.weekday())

if x.day == 1:
    if x.weekday() == 0:
        lastMonth = x.month - 1
        prev = lastDay(lastMonth)
elif x.day > 1:
    if x.weekday() == 0:
        lastMonth = x.month
        prev = prevDay(x.month, x.day)
    elif x.weekday() <= 5:
        prev = x.day - 1
        lastMonth = x.month

s = date(y, lastMonth, prev)
print("The last date of the week is:", s)
