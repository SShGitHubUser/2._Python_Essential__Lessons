""" Урок 9, завдання 3
Створіть модуль для отримання простих чисел. Імпортуйте його з іншого модуля. Імпортуйте його окремі
імена.
"""

# import lesson_9__task_3_module as primes

from lesson_9__task_3_module import check_primes, generate_n_primes


def main():
    print(check_primes(100))
    print(check_primes(29))

    print(list(generate_n_primes(10)))
    print(list(generate_n_primes(15)))


if __name__ == '__main__':
    main()
