""" Урок 10, завдання 2
Написати функцію, яка за допомогою регулярних виразів з файлу витягує дані про дату народження,
телефон та електронну адресу. Дані потрібно записати до іншого файлу.
"""

import re
import csv
from pprint import pprint


def extract_data(file_name: str) -> dict:
    result = {}
    pattern = re.compile(r'^(?P<FIO>\w+\s?\w+),'
                         r'.*\s(?P<birthday>\d{2}\.\d{2}\.\d{4})'
                         r'.*\s(?P<phone>\+\d{12})'
                         r'.*\s(?P<e_mail>\w+@\w+.\w+)')
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            result[pattern.search(line).group('FIO')] = pattern.search(line).groups()[1:]
            print(line)
            pprint(result)
    return result


def write_data(file_name: str, data: dict):
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['FIO', 'Birthday', 'Phone', 'E-mail'])
        for key, value in data.items():
            writer.writerow([key, *value])
            print(key, *value)


if __name__ == '__main__':
    people_data = extract_data('people.txt')
    write_data('people.csv', people_data)
