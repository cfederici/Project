#!/usr/bin/env python3

'''
Author: <Chris Federici>
Description: <The following code will be used to either return a date after a given amount of days or before a given amount of days>
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "returns true if the year is a leap year and false if it is not"
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:               # checking if the year provided is a modulus of 4 / 100 / 400
                return False
        else:
            return True
    else: 
        return False
    
def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    else:
        return mon_dict[month]

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_year(year):
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    
    if day > mon_max:
        mon += 1  
        if mon > 12:  # if the month selected is > 12 it will add a year 
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    "before() is the date for the previous day in DD/MM/YYYY"

    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # previous day
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_year(year):
        mon_max = 29
    else:
        mon_max = mon_dict[mon]

    if day < 1:
        mon -= 1
        if mon < 1:   # making sure the month is not below 1.
            year -= 1
            mon = 12
        if mon == 2 and leap_year(year):
            day = 29
        else:
            day = mon_dict[mon]# if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"

def usage(error):
    "Print an error message to the user"
    print("error: " + error)
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY num") 
    sys.exit()

def valid_date(date: str) -> bool:
    "Check the validity of a date in DD/MM/YYYY format."
    try:
        day, month, year = [int(x) for x in date.split('/')]
    except ValueError:   # Value error and printing of error message incase date isn't valid
        print('error in the validity of the date.')
        return False
    
    if year < 1500:    # Was not sure if i had to use specific year so just did <1500 to be sure
        return False
    else:
        if month < 1 or month > 12:
            return False
        else:
            if day < 1 or day > mon_max(month, year):
                return False
            else:
                return True

def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    if num > 0:
        todays_date = start_date
        for item in range(num):
            todays_date = after(todays_date)  #calling after variable with todays_date , elif number is less than 0, calling before function with (-num)
    elif num < 0:
        todays_date = start_date
        for item in range(-num):
            todays_date = before(todays_date)
    else:
        return start_date
    return todays_date

if __name__ == "__main__":    # a series of arguments, if statement and error handling. I used if not after researching and prefer it over !=
    # check length of arguments
    if len(sys.argv) != 3:
        usage("Invalid number of arguments.")
    # check first arg is a valid date
    if not valid_date(sys.argv[1]):
        usage("Date must be in DD/MM/YYYY format.")
    if not valid_date(sys.argv[1]):
        usage("Invalid date provided.")
    # check that second arg is a valid number (+/-)
    try:
        num = int(sys.argv[2]) 
    except ValueError:    # If argument is not a valid number for script , print a valueerror with usage message
        usage("The second argument must be a valid number that is positive or negative.")
    # call day_iter function to get end date, save to x
    x = day_iter(sys.argv[1], num)
    # print(f'The end date is {day_of_week(x)}, {x}.')
    print(f'The end date is {day_of_week(x)}, {x}.')
    pass