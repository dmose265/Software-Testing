# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:54:46 2020

@author: Dennis Mose
"""

while 1:
    print("Enter today's date in the form  MM DD YYYY");
    month = int(input("month: "))
    day = int(input("day: "))
    year= int(input("year: "))
    c1 = (1 <= day and day <= 31)
    c2 = (1 <= month and month <= 12)
    c3 = (1812 <= year and year <= 2012)
    if(1 <= day and day < 31):
        c1 = True
    if(1 <= month and month <= 12):
        c2 = True
    if(1812 <= year and year <= 2012):
        c3 = True
    if (c1 == False):
        print("Value of day not in the range of 1...........31")
    if (c2 == False):
        print("Value of month not in the range of 1........12")
    if (c3 == False):
        print("Value of year not in the range of 1812.......2012")
    elif c2== True and c1 == True and c3 == True:
        break
       
thirtyOneDays = [1, 3, 5, 7, 8, 10]
if day != 31 and (month in thirtyOneDays):
   tomorrowDay = day + 1
   tomorrowMonth = month
   tomorrowYear = year
        
elif day == 31 and (month in thirtyOneDays):
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
    if (year%4 == 0 and not(year%100 == 0)) or year%400 == 0:
        tomorrowDay = day + 1
        tomorrowMonth = month
        tomorrowYear = year
    
elif day == 28 and (month == 2):
        if (year%4==0 and not(year%100 == 0)) or year%400 == 0:
            tomorrowDay = 1
            tomorrowMonth = month + 1
            tomorrowYear = year
        
if day > 29  and (month == 2):
    print("Invalid input date.")
else:
    print("Tomorrow's date is {}-{}-{}".format(tomorrowMonth, tomorrowDay, tomorrowYear))    
