first, second, third = int(input('Введите первое число ')), int(input('Введите второе число ')), int(input('Введите последнее число '))
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)