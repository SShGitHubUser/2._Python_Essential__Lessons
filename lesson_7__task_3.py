""" Урок 7, завдання 3
Напишіть функцію-генератор для отримання n перших простих чисел.
"""


def generate_primes(n):
    primes = []
    num = max(primes) + 1 if primes else 2
    while True:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
            yield num
            if len(primes) == n:
                break
        else:
            num += 1


generator = generate_primes(5)
print(generator)
print(list(generator))
