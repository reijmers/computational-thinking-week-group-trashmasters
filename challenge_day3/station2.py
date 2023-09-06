import calendar
from datetime import date

def solution_station_2():

    d = date.today()
    print('Date is:', d)

    x = calendar.day_name[d.weekday()]
    print('Weekday name is:', x)