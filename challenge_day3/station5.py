import pandas as pd

data = pd.read_excel("names&groups.xlsx")

def solution_station5(name):
    row = data[data["Name"] == name]
    if not row.empty:
        return row.iloc[0]["Groups"]
    else:
        return None