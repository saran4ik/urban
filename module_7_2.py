def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w+', encoding='utf-8') as f:
        f.writelines("%s\n" % string for string in strings)
        f.seek(0)
        num_string = 1
        start_position = 0
        for line in iter(f.readline, ''):
            strings_positions[num_string, start_position] = line.strip()
            num_string += 1
            start_position = f.tell()
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
