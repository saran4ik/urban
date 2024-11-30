'''def all_variants(text: str):
    for start_index in range(len(text)):
        for end_index in range(len(text[start_index:])):
            print(text[start_index:][:end_index + 1])
    all_substrings = [text[start_index:][:end_index + 1] for start_index in range(len(text)) for end_index in range(len(text[start_index:]))]
    for substrings in all_substrings:
        print(substrings)'''


def all_variants(text: str):
    for start_index in range(1, len(text) + 1):  # перебираем все возможные последовательности
        for end_index in range(len(text) - start_index + 1):  # перебираем все возможные позиции
            yield text[end_index:end_index + start_index]  # возвращаем последовательность

# Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)
'''Вывод на консоль:
a
b
c
ab
bc
abc'''

