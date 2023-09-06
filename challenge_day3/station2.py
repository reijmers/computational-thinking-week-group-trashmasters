import calendar
from datetime import date

def solution_station_2():

    d = date.today()
    print('Date is:', d)

    x = calendar.day_name[d.weekday()]
    print('Weekday name is:', x)

    #月曜日 日曜日 土曜日 水曜日 火曜日 金曜日 木曜日