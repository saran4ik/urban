from os import walk, path
import time
for root, dirs, files in walk('.'):
    for file in files:
        filepath = path.join(root, file)  # Путь до файла
        filetime = path.getmtime(file)  # Время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Форматирование времени
        filesize = path.getsize(file)  # Размер файла в байтах
        parent_dir = path.dirname(path.abspath(root))  # Путь до родительской директории
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
