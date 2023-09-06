def solution_station_4(number):
    for i in range(2,number):
        if number%i == 0:
            return False
    return True

