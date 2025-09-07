a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

# a = 2, b = [3, 8]
# when lst[0] is changed it is a reassignment of the value in lst[0] from 
# 2 to 4, a is unaffeced. b however refers to a mutable object and when 
# lst[1][0] changes an element of the list it refers to, both references
# to the list reflect the change. 