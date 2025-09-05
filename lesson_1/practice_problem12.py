frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)

# the code will result in an error as frozensets are immutable and have no add
# method