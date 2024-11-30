def is_prime(func):
    def wrapper(*args, **kwargs):
        ans = func(*args, **kwargs)
        k = 0
        for i in range(2, ans // 2+1):
            if ans % i == 0:
                k = k+1
        if k <= 0:
            return f'Простое\n{ans}'
        else:
            return f'Составное\n{ans}'
    return wrapper
@ is_prime
def sum_three(a, b, c):
    answer = sum([a, b, c])
    return answer

# Пример:
result = sum_three(2, 3, 6)
print(result)
result1 = sum_three(12, 34, 16)
print(result1)

'''Результат консоли:
Простое
11'''
