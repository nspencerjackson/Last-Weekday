from datetime import date

def lastDay(inMonth):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(months[inMonth - 1]):
        temp = date(2021, inMonth, (i + 1)).weekday()
        if temp < 6:
            friday = i
    return friday

def prevDay(inMonth, inDay):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(months[inMonth - 1]):
        temp = date(2021, inMonth, (i + 1)).weekday()
        if temp < 6:
            if (i+1) < inDay:
                day = i
            else:
                break
    return day
