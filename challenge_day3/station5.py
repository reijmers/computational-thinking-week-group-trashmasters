import pandas as pd

data = pd.read_excel("C:\\Users\\Gur Levy\\computational-thinking-week-group-trashmasters\\challenge_day3\\namesgroups.xlsx")

def solution_station_5(name):
    row = data[data["Names"] == name]
    if not row.empty:
        return row.iloc[0]["Groups"]
    else:
        return None
    
name = "Gur"

group_number = solution_station_5(name)

print(group_number)



