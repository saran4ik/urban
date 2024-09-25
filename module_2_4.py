numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for n in range(2, len(numbers)+1):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
    else:
        not_primes.append(n)
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
