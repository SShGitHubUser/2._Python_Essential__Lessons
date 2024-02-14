""" Урок 8, завдання 2
Модифікуйте вихідний код сервісу зі скорочення посилань із попередніх двох уроків так, щоб він
зберігав базу посилань на диску і не «забув» при перезапуску. За бажанням можете ознайомитися з
модулем shelve (https://docs.python.org/3/library/shelve.html), який у даному випадку буде дуже
зручним та спростить виконання завдання.
"""

import shelve
from faker import Faker

fake = Faker()
with (shelve.open('short_url') as db):
    for _ in range(10):
        url = fake.url()
        uri = fake.uri_path()
        db[url] = url + uri
        print(url + uri)

with (shelve.open('short_url') as db):
    for key, value in db.items():
        print(f'short_URL: {key}, URL: {value}')
