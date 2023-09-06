import datetime

def solution_station_2():
    date_str = input("Enter a date (YYYY-MM_DD): ")

    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")

        day_of_week = date_obj.weekday()

        day_name = ["日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"][day_of_week]

        return date_str, day_name
    
    except ValueError:
        return None
    
result = solution_station_2()
print(f"The day of the week for {date_str} is {day_name}.")