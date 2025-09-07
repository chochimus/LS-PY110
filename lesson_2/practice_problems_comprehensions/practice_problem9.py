lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

answer = []
for dictionary in lst:
    subdict = {}
    all_even = True
    for values in dictionary.values():
        for num in values:
            if num % 2 != 0:
                all_even = False
    if all_even:
        answer.append(dictionary)

print(answer) # convert to comprehension

print([ dictionary
        for dictionary in lst
        if all(num % 2 == 0 for values in dictionary.values()
               for num in values)])