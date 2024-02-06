""" Урок 4, завдання 3
Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
Конструктор має генерувати виняток, якщо вказано неправильні дані. Введіть список працівників із
клавіатури. Виведіть усіх співробітників, які були прийняті після цього року.
"""

from faker import Faker

DEPARTMENT_LIST = ['Personnel', 'Finance', 'Marketing', 'Sales', 'IT', 'Logistics']
START_YEAR = 2015


class Employee:

    @staticmethod
    def validate_name(name):
        if not name.replace(' ', '').isalpha():
            raise ValueError(f'{name}: name must contain only letters and " "')
        return True

    @staticmethod
    def validate_surname(surname):
        if not surname.replace('-', '').isalpha():
            raise ValueError(f'{surname}: surname must contain only letters and "-"')
        return True

    @staticmethod
    def validate_department(department):
        if department not in DEPARTMENT_LIST:
            raise ValueError(f'{department}: department must be one of the following: ' + ', '.join(DEPARTMENT_LIST))
        return True

    @staticmethod
    def validate_year_of_start(year_of_start):
        if not year_of_start.isdigit():
            raise ValueError(f'{year_of_start}: year of start must contain only numbers')
        return True

    def __init__(self, name, surname, department, year_of_start):
        try:
            self.validate_name(name)
            self.name = name
        except ValueError as e:
            self.name = None
            print(e)
        try:
            self.validate_surname(surname)
            self.surname = surname
        except ValueError as e:
            self.surname = None
            print(e)
        try:
            self.validate_department(department)
            self.department = department
        except ValueError as e:
            self.department = None
            print(e)
        try:
            self.validate_year_of_start(year_of_start)
            self.year_of_start = int(year_of_start)
        except ValueError as e:
            self.year_of_start = None
            print(e)

    def __str__(self):
        return f'{self.name} {self.surname}, {self.department}, {self.year_of_start}'


# creating and filling a list with employees
fake = Faker()
employee_list = []
for _ in range(10):
    employee_list.append(Employee(fake.first_name(), fake.last_name(), fake.random_element(DEPARTMENT_LIST),
                                  str(fake.random_int(min=2000, max=2023))))
# print a list of employees with a year of start greater than the START_YEAR
for _ in range(len(employee_list)):
    if employee_list[_].year_of_start > START_YEAR:
        print(employee_list[_])
