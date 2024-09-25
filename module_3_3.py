def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(20, 'May', 2018)

values_list = [15, 'December']
print_params(*values_list, 1987)

values_dict = {'a': 3, 'b': 'September'}
print_params(**values_dict, c=False)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = [item]
    print(*list_my)


append_to_list(1215)

def append_to_list2(item, list_my=None):
    if list_my is None:
        list_my = [i for i in str(item)]
    print(*list_my)


append_to_list2(1215)
