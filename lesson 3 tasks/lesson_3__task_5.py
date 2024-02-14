""" Урок 3, завдання 5
Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від
класу Shape. Перевизначте їх методи. Створіть екземпляри відповідних класів та скористайтеся всіма
методами. В результаті повинно з’явитися зображення. Перегляньте їх.
"""

# Зроблено для арки та регулярного полігону

# example_7.py
from PIL import Image, ImageDraw


class Shape:
    def __init__(self):
        # Колір тла
        self.back_color = (155, 213, 117, 100)
        # Створюємо зображення 500 * 500
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)


class Arc(Shape):
    def draw(self):
        self.draw1.arc((75, 100, 175, 200), 0, 180, fill=(255, 255, 255))

    def erase(self):
        self.draw1.arc((75, 100, 175, 200), 0, 180, fill=self.back_color)

    def save(self):
        print("Image with arc was created")
        return self.im.save('draw-arc.png', quality=95)


class RegPolygon(Shape):
    def draw(self):
        self.draw1.regular_polygon((250, 250, 100), 5, fill=(255, 255, 255))

    def erase(self):
        self.draw1.regular_polygon((250, 250, 100), 5, fill=self.back_color)

    def save(self):
        print("Image with regular polygon was created")
        return self.im.save('draw-reg_polygon.png', quality=95)


def work_with_obj(obj):
    obj.draw()
    obj.save()


def update_obj(obj):
    obj.erase()
    obj.save()


def menu():
    while True:
        value = int(
            input('\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник'
                  '\n\t5. Зафарбувати коло\n\t6. Зафарбувати квадрат\n\t7. Зафарбувати трикутник\n\t'
                  '8. Cтворити арку\n\t9. Зафарбувати арку\n\t'
                  '10. Cтворити регулярний полігон\n\t11. Зафарбувати регулярний полігон\n\t'
                  '12. Вихід з програми\nОберіть необхідний пункт меню: '))
        if value == 1:
            s = Shape()
            s.save()
        elif value == 2:
            c = Circle()
            work_with_obj(c)
        elif value == 3:
            sq = Square()
            work_with_obj(sq)
        elif value == 4:
            t = Triangle()
            work_with_obj(t)
        elif value == 5:
            c = Circle()
            update_obj(c)
        elif value == 6:
            sq = Square()
            update_obj(sq)
        elif value == 7:
            t = Triangle()
            update_obj(t)
        elif value == 8:
            ar = Arc()
            work_with_obj(ar)
        elif value == 9:
            ar = Arc()
            update_obj(ar)
        elif value == 10:
            rp = RegPolygon()
            work_with_obj(rp)
        elif value == 11:
            rp = RegPolygon()
            update_obj(rp)
        elif value == 12:
            break
        else:
            print('Оберіть пункт меню корректно!!!')


if __name__ == '__main__':
    menu()
