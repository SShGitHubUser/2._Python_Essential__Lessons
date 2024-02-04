""" Урок 3, завдання 1
Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані?
Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).
"""


class Car:
    brand_list = ['BMW', 'Mercedes', 'Audi', 'Toyota', 'Hyundai', 'Kia', 'Ford', 'Volkswagen', 'Nissan']
    rgb_color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'white', 'black']

    def __init__(self, brand, model, year, rgb_color, price):
        self.__set_brand(brand)
        self.__set_year(year)
        self.model = model
        self._set_color(rgb_color)
        self._set_price(price)

    def get_brand(self):
        return f'Brand: {self.__brand}'

    def __set_brand(self, brand):
        if brand not in self.brand_list:
            self.__brand = 'n/a'
            print('Wrong brand, try again')
        else:
            self.__brand = brand

    def get_model(self):
        return f'model: {self.model}'

    def get_year(self):
        return f'year: {self.year}'

    def __set_year(self, year):
        if not year.isdigit() or int(year) < 1900:
            self.year = 'n/a'
            print('Wrong year, try again')
        else:
            self.year = year

    def get_color(self):
        return f'color: {self.__rgb_color}'

    def _set_color(self, rgb_color):
        if rgb_color not in self.rgb_color_list:
            self.__rgb_color = 'n/a'
            print('Wrong color, try again')
        else:
            self.__rgb_color = rgb_color

    def get_price(self):
        if self.price != 'n/a':
            return f'price: ${self.price:.2f}'
        else:
            return f'price: {self.price}'

    def _set_price(self, price):
        try:
            digit_price = float(price)
            if digit_price > 0:
                self.price = digit_price
            else:
                self.price = 'n/a'
                print('Wrong price, try again')
        except ValueError:
            self.price = 'n/a'
            print('Wrong price, try again')

    def __start_engine(self):
        pass

    def __stop_engine(self):
        pass

    def __check_engine(self):
        if self.__check_engine:
            print('Engine is working')
        else:
            print('Engine is not working')

    def __check_fuel(self):
        pass

    def __str__(self):
        return f'{self.get_brand()}, {self.get_model()}, {self.get_year()}, {self.get_color()}, {self.get_price()}'


car1 = Car('BMW', 'X5', '2020', 'red', '100000.00')
print(car1)
car2 = Car('Unknown', 'X5', '20', 'reddd', '-100000a')
print(car2)
