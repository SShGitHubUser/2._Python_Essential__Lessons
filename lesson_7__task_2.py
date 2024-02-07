""" Урок 7, завдання 2
Виведіть зі списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та
цикл
"""


def even_squares(iterable):
    for i in iterable:
        if i % 2 == 0:
            yield i ** 2


# variant 1

lst = range(10)
print(list(lst))

generator = even_squares(lst)
print(generator)
print(list(generator))

# variant 2

result = []
for item in lst:
    if item % 2 == 0:
        result.append(item ** 2)
print(result)

# variant 3

result = [x ** 2 for x in lst if x % 2 == 0]
print(result)
