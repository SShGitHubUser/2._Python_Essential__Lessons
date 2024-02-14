""" Урок 10, завдання 4
Напишіть функцію, яка буде аналізувати текст, що надходить до неї, і виводити тільки унікальні слова на
екран, загальну кількість слів і кількість унікальних слів.
"""

import re
from collections import Counter


def count_words(text: str):
    words = re.findall(r'\b\w+\b', text, re.I)
    result = Counter(words)
    for key, value in result.items():
        if value == 1:
            print(key, '\t', value)
    print('The number of words in the text:', sum(result.values()))
    print('The number of unique words in the text:', len(result))


if __name__ == '__main__':
    long_text = """Напишіть функцію, яка буде аналізувати текст, що надходить до неї, і виводити тільки унікальні
     слова на екран, загальну кількість слів і кількість унікальних слів."""
    count_words(long_text)
