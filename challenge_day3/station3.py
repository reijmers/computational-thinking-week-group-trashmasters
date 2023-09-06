import random

def solution_station_3():
    random_number = random.randint(1, 100)

    if random_number % 3 == 0:
        return "true"
    
    else:
        return "false"
    
result = solution_station_3()
print(f"Output: {result}")