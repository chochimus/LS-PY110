statement = "The Flintstones Rock"
statement_dict = {}
statement = statement.replace(' ', '')
for char in statement:
    statement_dict[char] = statement_dict.get(char, 0) + 1

print(statement_dict)