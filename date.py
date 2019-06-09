months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
no_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def convertDateToDay(date: str) -> str:
    year = date[-4:]
    month = date[2:5]
    day = date[:2]
    index = months.index(month)
    result = ''.join(str(sum([no_of_days[i] for i in range(index)])))
    if isLeapYear(year):
        return year + " " + str(int(result) + 1 + int(day))
    else:
        return year + " " + str(int(result) + int(day))

def isLeapYear(y: str) -> bool:
    return (int(y) % 4 == 0 and int(y) % 400 == 0) and (int(y) % 100 != 0)


import sys
date = ''.join(sys.argv[i] for i in range(1, len(sys.argv)))
print(convertDateToDay(date))

