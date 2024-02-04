""" Урок 3, завдання 2
Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting().
Обидва створюють різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії
цих двох об'єктів в одній функції (функція hello_friend).
"""


class English:
    @staticmethod
    def greeting():
        return 'Hello friend!'


class Spanish:
    @staticmethod
    def greeting():
        return 'Hola amigo!'


def hello_friend():
    for language in (english, spanish):
        print(type(language), language.greeting())


english = English()
spanish = Spanish()
hello_friend()
