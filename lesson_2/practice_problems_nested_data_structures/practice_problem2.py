lst1 = [1, [2, 3], 4]

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]

dict1 = {'first': [1, 2, [3]]}

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}

lst1[1][1] = 4
lst2[2] = 4
dict1['first'][2][0] = 4
dict2['a']['a'][2] = 4

print(lst1)
print(lst2)
print(dict1)
print(dict2)