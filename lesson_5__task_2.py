""" Урок 5, завдання 2
Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact,
sent_message. Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email,
job. Додати методи get_message. Створити екземпляри класів та дослідити стан об'єктів за допомогою
атрибутів: __dict__, __base__, __bases__. Роздрукувати інформацію на екрані.
"""

from pprint import pprint


class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f'{self.name} {self.surname}, {self.mob_phone}, {self.email}'

    @staticmethod
    def sent_message(name, surname):
        return f'Message sent to {name} {surname}'


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    @staticmethod
    def get_message(name, surname):
        return f'Message received from {name} {surname}'


contact_1 = Contact('Ivanov', 'Ivan', '30', '0123456789', 'abc@de')
contact_2 = UpdateContact('Petrov', 'Petr', '40', '9876543210', 'qwe@rt', 'programmer')

pprint('   class Contact')
pprint(contact_1.__dict__)
pprint(Contact.__dict__)
pprint(Contact.__base__)
pprint(Contact.__bases__)

pprint('   class UpdateContact')
pprint(contact_2.__dict__)
pprint(UpdateContact.__dict__)
pprint(UpdateContact.__base__)
pprint(UpdateContact.__bases__)
