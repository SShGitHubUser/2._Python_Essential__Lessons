""" Урок 6, завдання 1
Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable
"""

iterable = [1, 2, 3, 4, 5]
for item in iterable:
    print(item, end=' ')

print()

iterable = '12345'
for item in iterable:
    print(item, end=' ')
