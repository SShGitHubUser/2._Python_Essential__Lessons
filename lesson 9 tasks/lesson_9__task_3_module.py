""" Урок 9, завдання 3, модуль для отримання простих чисел
Створіть модуль для отримання простих чисел. Імпортуйте його з іншого модуля. Імпортуйте його окремі
імена.
"""


def check_primes(num):
    for i in range(2, round(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True


def generate_n_primes(n):
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
