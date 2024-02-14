""" Урок 1, завдання 2
Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків. Зробіть так,
щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.
"""


class Book:
    def __init__(self, author, title, public_year, genre):
        self.author = author
        self.title = title
        self.public_year = public_year
        self.genre = genre
        self.review_list = []

    def add_review(self, review):
        self.review_list.append(review)

    def __eq__(self, another):
        return self.author == another.author and self.title == another.title

    def __ne__(self, another):
        return self.author != another.author or self.title != another.title

    def __repr__(self):
        return f'Book: {self.title}, {self.author}, {self.genre}, {self.public_year}'

    def __str__(self):
        description = f'Book: {self.title}, {self.author}\n\n'
        description += 'Reviews:\n'
        for review in self.review_list:
            description += f'{review}\n\n'
        return description


class Review:
    def __init__(self, date_time, author, text, rating):
        self.date_time = date_time
        self.author = author
        self.text = text
        self.rating = rating

    def __repr__(self):
        return f'{self.date_time}, {self.author}, {self.rating}\n{self.text}'

    def __str__(self):
        return f'{self.date_time}, {self.author}\n{self.text}'


book = Book('Author 1', 'Title 1', 2000, 'Genre 1')
book.add_review(Review('2022-01-01 15:00', 'Author 1', 'Review Text 1', 5))
book.add_review(Review('2022-01-02 11:23', 'Author 2', 'Review Text 2', 4))
book.add_review(Review('2022-01-03 05:05', 'Author 3', 'Review Text 3', 3))

print(book)
