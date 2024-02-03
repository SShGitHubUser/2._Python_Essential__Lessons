""" Урок 2, завдання 6
Використовуючи код example_10, створіть декоратори @classmethod для формування переліку об'єктів,
які підрахують кількість повнолітніх людей в Україні й Америці.
"""

from datetime import date


class MyClass1:
    ukr_adulthood = 0
    usa_adulthood = 0

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, surname, name, birth_year):
        return cls(surname, name, date.today().year - birth_year)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @classmethod
    def count_ukr_adulthood(cls, age):
        if age >= 18:
            cls.ukr_adulthood += 1
        return cls.ukr_adulthood

    @classmethod
    def count_usa_adulthood(cls, age):
        if age >= 21:
            cls.usa_adulthood += 1
        return cls.usa_adulthood


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.count_ukr_adulthood(m_per1.age)
m_per1.print_info()

m_per2 = MyClass1.from_birth_year('Dovzhenko', 'Bogdan', 2000)
m_per2.count_ukr_adulthood(m_per2.age)
m_per2.print_info()

m_per3 = MyClass1('Smith', 'John', 22)
m_per3.count_usa_adulthood(m_per2.age)
m_per3.print_info()

print('Number of adults in Ukraine:', MyClass1.ukr_adulthood)
print('Number of adults in USA:', MyClass1.usa_adulthood)
