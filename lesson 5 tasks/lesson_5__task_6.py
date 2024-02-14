""" Урок 5, завдання 6
Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі Contact та
UpdateContact.
"""

import inspect


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


print('   class Contact')
contact_1 = Contact('Ivanov', 'Ivan', '30', '0123456789', 'abc@de')
contact_1_attributes = dir(contact_1)
contact_1_methods = [attr for attr in contact_1_attributes if inspect.ismethod(getattr(contact_1, attr))]
for _ in contact_1_methods:
    print(_)

print('   class UpdateContact')
contact_2 = UpdateContact('Petrov', 'Petr', '40', '9876543210', 'qwe@rt', 'programmer')
contact_2_attributes = dir(contact_2)
contact_2_methods = [attr for attr in contact_2_attributes if inspect.ismethod(getattr(contact_2, attr))]
for _ in contact_2_methods:
    print(_)
