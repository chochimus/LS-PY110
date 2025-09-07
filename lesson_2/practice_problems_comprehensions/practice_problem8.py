dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

new_lst = []

for subdict in dict1.values():
    colors = []
    if subdict['type'] == 'fruit':
        for color in subdict['colors']:
            colors.append(color.capitalize())
        new_lst.append(colors)
    else:
        new_lst.append(subdict['size'].upper())

print(new_lst)

def add_element(element):
    if element['type'] == 'fruit':
        return [color.capitalize() for color in element['colors']]
    else:
        return element['size'].upper()
print([add_element(element) for element in dict1.values()])