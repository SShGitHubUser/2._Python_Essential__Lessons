""" Урок 9, завдання 1
Перепишіть домашнє завдання попереднього уроку (сервіс для скорочення посилань) таким чином, щоб
у нього була основна частина, яка відповідала би за логіку роботи та надавала узагальнений інтерфейс, і
модуль представлення, який відповідав би за взаємодію з користувачем. При заміні останнього на
інший, який взаємодіє з користувачем в інший спосіб, програма має продовжувати коректно працювати.
"""

import shelve
import lesson_9__task_1_module as user


def main():
    short_url_list = []
    with (shelve.open('short_url') as db):
        for _ in range(10):
            short_url = user.set_short_url()
            url = user.set_url(short_url)
            db[short_url] = url
            short_url_list.append(short_url)

    with (shelve.open('short_url') as db):
        for _ in range(len(short_url_list)):
            key = user.get_url(short_url_list)
            print(f'short_URL: {key}, URL: {db.get(key)}')


if __name__ == '__main__':
    main()
