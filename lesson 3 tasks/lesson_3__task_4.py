""" Урок 3, завдання 4
Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль фрази
відповідно "Hello from Base" та "Hello from Child".
"""


class Base:
    def method(self):
        print('Hello from Base')
        return


class Child(Base):
    def method(self):
        print('Hello from Child')
        return


base = Base()
child = Child()
base.method()
child.method()
