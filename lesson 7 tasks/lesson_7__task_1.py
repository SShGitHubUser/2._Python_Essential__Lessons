""" Урок 7, завдання 1
Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
"""


def reverse_list(iterable):
    for i in range(len(iterable)):
        yield iterable[len(iterable) - 1 - i]


iter = [1, 2, 3, 4, 5]
generator = reverse_list(iter)
print(generator)
print(iter)
print(list(generator))

iter = 'abcde'
generator = reverse_list(iter)
print(iter)
print(''.join(list(generator)))
