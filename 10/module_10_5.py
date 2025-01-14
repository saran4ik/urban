import multiprocessing
from datetime import datetime as dt

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf8') as file1:
        for line in file1:
            all_data.append(line)

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start_l = dt.now()

for file in files:
    read_info(file)
end_l = dt.now()
time_line = end_l - start_l
print(f'Время работы линейного вызова : {time_line}')

if __name__ == '__main__':
    start_m = dt.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end_m = dt.now()
    time_multi = end_m - start_m
    print(f'Время работы мультипроцесса : {time_multi}')