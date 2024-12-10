from time import sleep
from datetime import datetime as dt
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


func_start_time = dt.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

func_end_time = dt.now()
func_time = func_end_time - func_start_time

print(f'Работа функций {func_time}')

thread_start_time = dt.now()

thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

thread_end_time = dt.now()
thread_time = thread_end_time - thread_start_time
print(f'Работа потоков {thread_time}')

print(f'Потоки быстрее функций на {func_time - thread_time} секунд')
