""" Урок 10, завдання 5
З клавіатури вводиться рядок, в якому є інформація про прізвище, ім'я, дату народження, електронну
адресу та відгук про курси учня. Написати функцію, яка, використовуючи регулярні вирази, витягне дані з
рядка і поверне словник.
"""

import re
from pprint import pprint


def parse_feedback(feedback: str) -> dict:
    info = re.search(r'^(?P<surname>\w+)\s*'
                     r'(?P<name>\w+),'
                     r'.*\s(?P<birthday>\d{2}\.\d{2}\.\d{4})'
                     r'.*\s(?P<phone>\+\d{12})'
                     r'.*\s(?P<e_mail>\w+@\w+.\w+)'
                     r'.?\s*(?P<feedback>.*)',
                     feedback)
    result = {'surname': info.group('surname'),
              'name': info.group('name'),
              'birthday': info.group('birthday'),
              'e-mail': info.group('e_mail'),
              'feedback': info.group('feedback')}
    return result


if __name__ == '__main__':
    # text = input('Enter feedback: ')
    text = 'Ivanov Ivan, 01.01.1990, +380123456789, ivanov@example.com. Good feedback'
    parse_result = parse_feedback(text)
    pprint(parse_result)
