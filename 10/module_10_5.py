import multiprocessing
from datetime import datetime as dt

def read_info(filename):
    all_data = []
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            if line:
                all_data.append(line)
    print(f'{len(all_data)} кол-во не пустых строк в файле {filename}')
#        all_data = [line for line in file if line] # по времени особо разницы нет

filenames = [f'./file {number}.txt' for number in range(1, 5)]
#print(filenames)


if __name__ == '__main__':
    start_l = dt.now()
    for filename in filenames:
        read_info(filename)
    end_l = dt.now()
    time_line = end_l - start_l
    print(f'{time_line} (линейный)')

    start_m = dt.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_m = dt.now()
    time_multi = end_m - start_m
    print(f'{time_multi} (многопроцессный)')