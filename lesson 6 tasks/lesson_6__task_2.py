""" Урок 6, завдання 2
Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList, додавши методи
очищення списку, додавання елемента у довільне місце списку, видалення елемента з кінця та
довільного місця списку.
"""


#    Methods added:
# def clear(self):
# def insert(self, position, element):
# def pop(self, position=-1) -> _ListNode:

# example_5.py


class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def clear(self):
        """Очистка списка"""

        while self._head is not None:
            node = self._head.next
            del self._head
            self._head = node
            print(self)
        self._length = 0
        self._head = self._tail = None

    def insert(self, position, element):
        """Добавление элемента в произвольную позицию списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)
        # Добавляем элемент
        if position <= 0:
            if self._length == 0:
                self.append(element)
                del node
            else:
                node.next = self._head
                self._head.prev = node
                self._head = node
                self._length += 1
        elif 0 < position < self._length:
            # Поиск позиции в списке, для простоты ищем только от начала к концу списка
            node_left = self._head
            for _ in range(position - 1):
                node_left = node_left.next
            node_right = node_left.next
            # Вставка элемента в заданную позицию
            node_left.next = node
            node.prev = node_left
            node.next = node_right
            node_right.prev = node
            self._length += 1
        else:
            self.append(element)

    def pop(self, position=-1) -> _ListNode:
        """Удаление элемента из произвольной позиции списка. Если индекс не указан, удаляется последний элемент.
           Если индекс находится за пределами последовательности, иницируется IndexError"""

        if position == -1:
            position = self._length - 1
        if 0 <= position < self._length:
            # Поиск позиции в списке, для простоты ищем только от начала к концу списка
            node = self._head
            for _ in range(position):
                node = node.next
            # Удаление элемента из списка
            if position == 0:
                self._head = node.next
                self._head.prev = None
            elif position == self._length - 1:
                self._tail = node.prev
                self._tail.next = None
            else:
                node_left = node.prev
                node_right = node.next
                node_left.next = node_right
                node_right.prev = node_left
            self._length -= 1
            return node
        else:
            raise IndexError('pop index out of range')

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    # Создание списка
    my_list = MyList([1, 2, 3, 4, 5])

    # Вывод длины списка
    print(len(my_list))

    # Вывод самого списка
    print(my_list)

    print()

    # Обход списка
    for element in my_list:
        print(element)

    # Вставка элемента в список
    print()
    my_list.insert(1, '11')
    print(my_list)

    # Удаление элемента из списка
    print()

    my_list.pop()
    print(my_list)

    my_list.pop(2)
    print(my_list)

    # Очистка списка
    my_list.clear()
    print(my_list)


if __name__ == '__main__':
    main()
