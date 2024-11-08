my_dict = {'Black Widow': 1984, 'Iron Man':  1965, 'Spider Men': 1975, 'Batman':  1974}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Iron Man'))
print('Not existing value:', my_dict.get('Denis'))
my_dict['Daredevil'] = 1972
my_dict['Neo'] = 1964
print('Deleted value:', my_dict.pop('Batman'))
print('Modified dictionary:', my_dict)
print('')
my_set = {12, 'FireBird', 3.14, 'Icecream'}
print('Set', my_set)
my_set.add(77)
my_set.add((48, 25, 16))
my_set.discard(12)
print('Modified set: ', my_set)
