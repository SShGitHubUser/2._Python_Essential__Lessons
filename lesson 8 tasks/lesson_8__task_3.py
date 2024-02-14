""" Урок 8, завдання 3
Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON
"""

import pickle
import json

goods = [
    {'id': 1, 'name': 'Notebook', 'price': 10000},
    {'id': 2, 'name': 'Smartphone', 'price': 5000},
    {'id': 3, 'name': 'Tablet', 'price': 3700}
]

with open('goods.pkl', 'wb') as f:
    pickle.dump(goods, f)

with open('goods.json', 'w') as f:
    json.dump(goods, f)
