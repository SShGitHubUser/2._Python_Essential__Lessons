""" Урок 4, завдання 4
Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе
певне значення, і перехопіть цей виняток під час виклику функції.
"""


class BirthdayYearError(Exception):
    def __init__(self, birthday_year: str):
        self.message = 'Incorrect birthday year'
        self.birthday_year = birthday_year
        super().__init__(self.message)

    def __str__(self):
        return f'Incorrect birthday year: {self.birthday_year}'


def set_birthday_year(year: str):
    try:
        if not all([year.isdigit(), len(year) in [2, 4]]):
            raise BirthdayYearError(year)
        else:
            print(f'Birthday year is {year}')
    except BirthdayYearError as e:
        print(e)


set_birthday_year('2000')
set_birthday_year('20')
set_birthday_year('202')
set_birthday_year('abcd')
