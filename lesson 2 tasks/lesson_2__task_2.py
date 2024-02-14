""" Урок 2, завдання 2
Опишіть класи графічного об'єкта, прямокутника й об'єкта, який може обробляти натискання мишки.
Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на
кнопку.
"""


class Rectangle:
    def __init__(self, height, width):
        self.width = width
        self.height = height

    def draw(self):
        for i1 in range(self.height):
            for i2 in range(self.width):
                if any([i1 == 0, i1 == self.height - 1, i2 == 0, i2 == self.width - 1]):
                    print('*', end='')
                else:
                    print(' ', end='')
            print()


class MouseClick:

    @staticmethod
    def mouse_click():
        print('Mouse button clicked')


class Button(Rectangle, MouseClick):

    def __init__(self, height, width):
        super().__init__(height, width)


rectangle = Rectangle(3, 7)
button = Button(3, 7)
button.draw()
input('Press any key to continue...')
button.mouse_click()
