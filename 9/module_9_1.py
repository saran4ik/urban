def apply_all_func(int_list, *functions):
    result = {}
    try:
        for function in functions:
            result[str(function.__name__)] = function(int_list)
        return result
    except:
        return 'Ошибка'


#Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, '20', 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
#Вывод на консоль:
#{'max': 20, 'min': 6}
#{'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
