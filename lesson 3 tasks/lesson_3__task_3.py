""" Урок 3, завдання 3
Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як
властивості. Ознайомтеся з декоратором property у Python. Створіть клас, що описує температуру і
дозволяє задавати та отримувати температуру за шкалою Цельсія та Фаренгейта, причому дані можуть
бути задані в одній шкалі, а отримані в іншій.
"""


class Temperature:

    def __init__(self):
        self.celsius = None
        self.fahrenheit = None

    @property
    def in_celsius(self):
        if self.celsius is None:
            return (self.fahrenheit - 32) * 5 / 9
        else:
            return self.celsius

    @in_celsius.setter
    def in_celsius(self, value):
        self.celsius = value
        self.fahrenheit = None

    @property
    def in_fahrenheit(self):
        if self.fahrenheit is None:
            return self.celsius * 9 / 5 + 32
        else:
            return self.fahrenheit

    @in_fahrenheit.setter
    def in_fahrenheit(self, value):
        self.celsius = None
        self.fahrenheit = value


temp = Temperature()
temp.in_celsius = 0
print(f'{temp.in_celsius:.1f} C = {temp.in_fahrenheit:.1f} F')
temp.in_celsius = 100
print(f'{temp.in_celsius:.1f} C = {temp.in_fahrenheit:.1f} F')
temp.in_fahrenheit = 0
print(f'{temp.in_fahrenheit:.1f} F = {temp.in_celsius:.1f} C')
temp.in_fahrenheit = 100
print(f'{temp.in_fahrenheit:.1f} F = {temp.in_celsius:.1f} C')
