"""
    inputs: integer representing the number of a particular row
    output: integer representing the sum of all the integers in that row

    requirements:
        explicit:
            - sequence of integers
            - sequence begins with 2
            - integers are consecutive
            - all integers are even
            - sequence is grouped into rows
            - each row incrementally larger than the last: 1, 2, 3, ...
        implicit:
            - row 1 has 1 element, 2 has 2, etc.
        
        sequence:
            - 2
            - 4, 6
            - 8, 10, 12
            - 14, 16, 18, 20

    examples:
    Row number: 1 -> Sum of integers in row: 2
    Row number: 2 -> Sum of integers in row: 10
    Row number: 4 -> Sum of integers in row: 68

    data structures:

"""

def get_solution(number):
    sequence = []
    current = 2
    for i in range(1, number + 1):
        row = []
        for _ in range(i):
            row.append(current)
            current += 2
        sequence.append(row)
    return sum(sequence[-1])


print(get_solution(3))
print(get_solution(1))
print(get_solution(4))
