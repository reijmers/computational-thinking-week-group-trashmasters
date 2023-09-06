import datetime

def solution_station_2(date_str):

    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")

    day_of_week = date_obj.weekday()

    day_name = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

    return day_name[day_of_week]
    
#Takes the day of the year and outputs what day of the week it is in Japanese

    