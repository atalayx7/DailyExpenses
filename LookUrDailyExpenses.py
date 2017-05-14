'''
It calculates the daily expenses that you spent, the average, and total amount.
'''

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7.77, 8.77, 8.66, 9.99]  # enter your daily expenses here


def average():
    t = []
    total = 0.0
    count = 0
    for i in range(len(x)):
        total += x[i]
        count += 1
    print("Total outgoing during", count, "day : %.02f" % total, " €")
    print("The average in a day : %.02f" % (total / count), " €")


def main():
    t = []
    global theYear
    theYear = input("Enter the first date : e.g., 31:03:2017     ")
    t += theYear.split(":")

    firstDay = (int)(t[0])
    global theMonth
    theMonth = (int)(t[1])
    theYear = (int)(t[2])

    for i, j in zip(dateCal(firstDay, theMonth, theYear), x):
        print("{} -> {} €".format(i, j))


def dateCal(day, month, year):
    lastDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    theList = []
    _month = month
    _day = day
    if _month == 2:

        print("_month", _month)
        if isLeapYear(theYear):

            lastDay[1] = 29
        else:
            pass
    for i in range(len(x)):

        if ((lastDay[month - 1] == _day) and (months[_month - 1]) == _month):
            theList += [("{}:{}:{}".format(_day, month, year))]
            _day = 1
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
        else:
            theList += [("{}:{}:{}".format(_day, month, year))]

            _day = _day + 1

    return theList


def isLeapYear(year):
    if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        return True
    else:
        return False


main()
average()
