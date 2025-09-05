def less_than(upper_limit):
    numbers = []
    candidate = 0

    while candidate < upper_limit:
        candidate += 1
        numbers.append(candidate)

    return numbers


print(less_than(5))