lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

lst2 = []
for dict in lst:
    new_dict = {}
    for key,value in dict.items():
        new_dict[key] = value + 1
    lst2.append(new_dict)
print(lst2)

print([{key: value + 1 for key, value in dictionary.items()} 
                        for dictionary in lst])