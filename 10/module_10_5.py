import multiprocessing
from datetime import datetime as dt

def read_info(filename):
    all_data = []
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]
start_l = dt.now()

for filename in filenames:
    read_info(filename)
end_l = dt.now()
time_line = end_l - start_l
print(f'Время работы линейного вызова : {time_line}')

if __name__ == '__main__':
    start_m = dt.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_m = dt.now()
    time_multi = end_m - start_m
    print(f'Время работы мультипроцесса : {time_multi}')