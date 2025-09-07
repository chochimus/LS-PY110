lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_lst = []
for element in lst:
    new_lst.append(sorted(element))
print(new_lst)

print([sorted(element) for element in lst])