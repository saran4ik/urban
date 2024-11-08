class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # список файлов

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:  # открываем файл
                words = []
                for string in f:  # читаем строки из файла
                    string = string.lower()  # приводим строку к нижнему регистру
                    marks = [',', '.', '=', '!', '?', ';', ':', ' - ']  # знаки препинания
                    string = ''.join(s for s in string if s not in marks)  # удаляем все знаки препинания
                    words.extend(string.split())  # разбиваем строку на слова
                all_words[file_name] = words  # добавляем слова в словарь
        return all_words

    def find(self, word):
        position = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:  # если слово встречается в тексте
                position[name] = words.index(word.lower()) + 1  # определяем позицию
        return position  # возвращаем позицию

    def count(self, word):
        counters = {}
        for name, words in self.get_all_words().items():
            words_count = words.count(word.lower())  # количество слов
            counters[name] = words_count  # добавляем слово и кол-во в словарь
        return counters


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))