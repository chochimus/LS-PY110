lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = []

for sublst in lst:
    new_sublst = []
    for ele in sublst:
        if ele % 3 == 0:
            new_sublst.append(ele)
    new_lst.append(new_sublst)

print(new_lst)


print([[ele for ele in sublst if ele % 3 == 0] for sublst in lst])