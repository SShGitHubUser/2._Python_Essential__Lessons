""" Урок 2, завдання 5
Використовуючи код example_10, створіть декоратор @staticmethod для визначення повноліття людини
в Україні й Америці.
"""

from datetime import date


class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, surname, name, birth_year):
        return cls(surname, name, date.today().year - birth_year)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @staticmethod
    def check_ukr_adulthood(age):
        return age >= 18

    @staticmethod
    def check_usa_adulthood(age):
        return age >= 21


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
print('Adults in Ukraine:', m_per1.check_ukr_adulthood(m_per1.age))
print('Adults in USA:', m_per1.check_usa_adulthood(m_per1.age))
m_per1.print_info()

m_per2 = MyClass1.from_birth_year('Dovzhenko', 'Bogdan', 2000)
print('Adults in Ukraine:', m_per2.check_ukr_adulthood(m_per2.age))
print('Adults in Ukraine:', m_per2.check_usa_adulthood(m_per2.age))
m_per2.print_info()
