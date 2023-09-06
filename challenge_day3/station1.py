#fibonacci sequence

def solution_station_1(n):

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a

#fibonnaci sequence
#function returns the fibonacci number at the nth position
