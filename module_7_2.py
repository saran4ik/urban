def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines("%s\n" % string for string in strings)
        print('Write finished')
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_index = [0]
        while f.readline():
            lines_index.append(f.tell())
        f.seek(0)
        file_strings = f.read().splitlines()
        num_string = 1
        for i in range(len(file_strings)):
            strings_positions[num_string, lines_index[i]] = file_strings[i]
            num_string += 1
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
