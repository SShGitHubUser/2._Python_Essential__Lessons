""" Урок 1, завдання 4
Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів,
доступних для продажу, і функцію продажу заданого автомобіля.
"""


class Car:
    def __init__(self, model, year, color, number):
        self.model = model
        self.year = year
        self.color = color
        self.number = number


class Salon:

    def __init__(self):
        self.cars = list()

    def add_car(self, car):
        self.cars.append(car)

    def sell_car(self, car):
        self.cars.remove(car)
