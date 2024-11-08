n = int(input("Введите число от 3 до 21 "))
list_n =[]
if n in range(3, 21):
    print(f'Ваше число {n}')
    for i in range(1, n):
        for j in range(1, n):
            if i and j not in list_n and i != j and n % (i + j) == 0:
                list_n.append(i)
                list_n.append(j)
    print("Пароль:", "".join(map(str,list_n)))
else:
    print("Введеные данные не соответствуют условиям")
