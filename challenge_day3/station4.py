def solution_station_4(number):
    if number == 1:
        return False
    else:
        for i in range(2,number):
            if number%i == 0:
                return False
        return True

#prime numbers
#function returns true if prime, and false if composite