""" Урок 6, завдання 3
Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
"""


class ReverseIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.iterable[self.index]


my_list = [1, 2, 3, 4, 5]
reverse_iterator = ReverseIterator(my_list)
for item in reverse_iterator:
    print(item, end=' ')

print()

my_list = 'abcde'
reverse_iterator = ReverseIterator(my_list)
for item in reverse_iterator:
    print(item, end=' ')
