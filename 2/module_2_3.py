my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
while n in range(len(my_list)) and my_list[n] >= 0:
    if my_list[n] > 0:
        print(my_list[n])
    n += 1
