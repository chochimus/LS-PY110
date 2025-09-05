"""
input: list of strings
output: list of strings sorted by highest number of adjacent consonants

requirements:
    explicit:
        - sort list based on highest number of adjacent consonants
        - if two strings contain the same number, they should retain order in relation to eachother
        - spaces can be ignored 
    implicit:
        -strings may contain multiple words
        - no empty strings
        - may have 0 adjacent consonants
        - descending order

questions:
    can there be empty strings?
    ascending or descending?
    is case important


algorithm:

1. given a list of strings
2. go over each string and determine the number of adjacent consonants for each string
3. sort based on number of consonants

- strip input string
- initialize max consonant count to zero
- initialize adjacent string to an empty string
- for each letter in the input string:
    -if letter is a consonant:
      concatenate it to adjacent string
    else:
      if adjacent string length is greater than current max consonant count:
        if length is greater than 1:
            set max consonant count to length
      reset adjacent string to empty string
- return max consonant count
"""

def count_max_adjacent_consonants(string):
    no_spaces = ''.join(string.split())
    max_consonants = 0
    adjacent_string = ''

    for char in no_spaces:
        if char not in 'aeiou':
            adjacent_string += char
        else:
            if len(adjacent_string) > 1:
                max_consonants = max(max_consonants, len(adjacent_string))
            adjacent_string = ""

    if len(adjacent_string) > 1:
        max_consonants = max(max_consonants,len(adjacent_string))
    return max_consonants

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# Expected: ['dddaa', 'ccaa', 'aa', 'baa']
# Actual:   ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# Expected: ['salt pan', 'can can', 'batman', 'toucan']
# Actual:   ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# Expected: ['bar', 'car', 'far', 'jar']
# Actual:   ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# Expected: ['month', 'day', 'week', 'year']
# Actual:   ['day', 'week', 'month', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# Expected: ['xxxx', 'xxxb', 'xxxa']
# Actual:   ['xxxa', 'xxxx', 'xxxb']