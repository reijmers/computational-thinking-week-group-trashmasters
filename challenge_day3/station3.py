import random

def solution_station_3():
    random_number = random.randint(1, 100)

    if random_number % 3 == 0:
        return random_number, "true"
    
    else:
        return random_number, "false"
    
random_number, result = solution_station_3()

print(f"Input: {random_number}")
print(f"Output: {result}")