""" Урок 10, завдання 1
Написати функцію, яка за допомогою регулярних виразів розбиває текст на окремі слова і знаходить
частоту окремих слів.
"""

import re
from collections import Counter
from pprint import pprint


def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)


if __name__ == '__main__':
    word_counts = count_words("""Написати функцію, яка за допомогою регулярних виразів розбиває текст на 
                                 окремі слова і знаходить частоту окремих слів.""")
    print('The number of words in the text:', sum(word_counts.values()))
    print('The number of unique words in the text:', len(word_counts))
    pprint(word_counts)
