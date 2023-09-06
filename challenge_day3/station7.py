def solution_station_7(input: str) -> float:

    variables = {"a": 3, "b": -1, "c": 4, "d": 7, "e": 0.5}
    output = 0
    
    terms = input.split("+")
    for term in terms:
        factors = term.split("*")
        term_output = 1
        for factor in factors:
            if factor in variables:
                term_result *= variables[factor]
            else:
                term_result *= float(factor)
        output += term_result

    return output

