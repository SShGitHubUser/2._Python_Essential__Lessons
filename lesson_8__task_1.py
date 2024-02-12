""" Урок 8, завдання 1
Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел.
Створіть ще один скрипт, який читає числа з файлу та виводить на екран їхню суму.
"""

import random

with open('numbers.txt', 'w') as file:
    for _ in range(10000):
        file.write(f'{random.random():.3}\n')

summ = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        summ += float(line)
    print(summ)
