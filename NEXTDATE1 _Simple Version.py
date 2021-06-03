# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:58:03 2020

@author: Dennis Mose
"""


month = int(input("month: "))
day = int(input("day: "))
year = int(input("year: "))
ThirtyOneDays = [1, 3, 5, 7, 8, 10]

if day != 31 and (month in ThirtyOneDays):
    tomorrowDay = day + 1
    tomorrowMonth = month
    tomorrowYear = year
elif day == 31 and (month in ThirtyOneDays):
    tomorrowDay = 1
    tomorrowMonth = month + 1
    tomorrowYear = year
    
thirtyDays = [4, 6, 9, 11]

if day == 30 and (month in thirtyDays):
    tomorrowDay = 1
    tomorrowMonth = month +1
    tomorrowYear = year
    
elif day != 30 and (month in thirtyDays):
    tomorrowDay = day + 1
    tomorrowMonth = month 
    tomorrowYear = year


if day != 31 and (month == 12):
    tomorrowDay = day + 1
    tomorrowMonth = month
    tomorrowYear = year
    
elif day == 31 and (month == 12):
    tomorrowDay = 1
    tomorrowMonth = 1
    if year == 2012:
        print("2012 is over")
        tomorrowYear = year +1
    
if day != 28 and (month == 2) :
    if (year %4 == 0 and not(year %100 == 0)) or year%400 == 0:
        tomorrowDay = day + 1
        tomorrowMonth = month
        tomorrowYear = year
elif day == 28 and (month == 2):
    if (year %4 == 0 and not(year %100 == 0)) or year %400 == 0:
        tomorrowDay = 1
        tomorrowMonth = month + 1
        tomorrowYear = year
    else:
        print("Cannot have Feb.", day)

print("Tomorrow's date is {}-{}-{}".format(tomorrowMonth, tomorrowDay, tomorrowYear))