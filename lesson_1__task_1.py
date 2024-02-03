""" Урок 1, завдання 1
Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та
жанр. Створіть кілька різних книжок. Визначте для нього операції перевірки на рівність та нерівність,
методи _repr_ та _str_.
"""


class Book:
    def __init__(self, author, title, public_year, genre):
        self.author = author
        self.title = title
        self.public_year = public_year
        self.genre = genre

    def __eq__(self, another):
        return self.author == another.author and self.title == another.title

    def __ne__(self, another):
        return self.author != another.author or self.title != another.title

    def __repr__(self):
        return f'Book: {self.title}, {self.author}, {self.genre}, {self.public_year}'

    def __str__(self):
        return f'Book: {self.title}, {self.author}'


book_1 = Book('Author 1', 'Title 1', 2000, 'Genre 1')
book_2 = Book('Author 2', 'Title 2', 2001, 'Genre 2')
book_3 = Book('Author 1', 'Title 1', 2010, 'Genre 1')
book_4 = Book('Author 3', 'Title 3', 2002, 'Genre 3')
book_5 = Book('Author 2', 'Title 4', 2003, 'Genre 4')

print(book_1 == book_2)
print(book_1 == book_3)
print(book_2 == book_5)
