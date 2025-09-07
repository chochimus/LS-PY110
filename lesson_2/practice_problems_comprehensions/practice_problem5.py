lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_odd(sublist):
    sum = 0
    for num in sublist:
        if num % 2 != 0:
            sum += num
    return sum

print(sorted(lst, key=sum_odd))

def sum_odd2(sublist):
    return sum([num for num in sublist if num % 2 != 0])

print(sorted(lst, key=sum_odd2))