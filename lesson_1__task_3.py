""" Урок 1, завдання 3
Ознайомтеся зі спеціальними методами в Python, використовуючи посилання в кінці уроку, і навчіться
використовувати ті з них, призначення яких ви можете зрозуміти. Повертайтеся до цієї теми протягом
усього курсу та вивчайте спеціальні методи, що відповідають темам кожного уроку.
"""


class Book:

    def __new__(cls, *args, **kwargs):
        print('Создан новый экземпляр книги')
        return super().__new__(cls)

    def __init__(self, author, title, public_year, genre):
        print('__doc__ =', self.__doc__)
        print('__class__ =', self.__class__)
        print('__dict__ =', self.__dict__)
        self.author = author
        self.title = title
        self.public_year = public_year
        self.genre = genre

    def __str__(self):
        return f'Book: {self.title}, {self.author}'

    def __repr__(self):
        return f'Class: Book'

    def __del__(self):
        print('Book deleting')

    def __eq__(self, another):
        return self.author == another.author and self.title == another.title

    def __ne__(self, another):
        return self.author != another.author or self.title != another.title


book = Book('Author 1', 'Title 1', 2000, 'Genre 1')
