def custom_write(file_name, strings):
    strings_positions = {}  # будущий словарь
    with open(file_name, 'w+', encoding='utf-8') as f:  # создаем файл c возможностью чтения
        f.writelines("%s\n" % string for string in strings)  # записываем в файл все строки через разрыв строки
        f.seek(0)  # переходим на начало файла
        num_string = 1  # счетчик строк
        start_position = 0  # счетчик позиции
        for line in iter(f.readline, ''):  # перебираем файл
            strings_positions[num_string, start_position] = line.strip()  # в словарь номер строки, позицию и строку
            num_string += 1  # увеличиваем счетчик строк
            start_position = f.tell()  # увеличиваем счетчик позиции на количество байтов строки
    return strings_positions  # возвращаем словарь


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
