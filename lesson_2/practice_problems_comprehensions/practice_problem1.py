munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

age = 0
for name,info in munsters.items():
    if info['gender'] == 'male':
        age += info['age']
print(age)

print(sum([munster['age'] for munster in munsters.values()
           if munster['gender'] == 'male']))