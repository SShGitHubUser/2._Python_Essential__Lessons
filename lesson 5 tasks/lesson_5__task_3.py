""" Урок 5, завдання 3
Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr(). Застосувати
ці функції до кожного з атрибутів класів, подивитися до чого це призводить.
"""


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

# hasattr(), getattr(), setattr(), delattr()
print('   class Contact')
print(hasattr(contact_1, 'name'))
print(getattr(contact_1, 'name'))
setattr(contact_1, 'name', 'Ivanko')
print(getattr(contact_1, 'name'))
delattr(contact_1, 'name')
print(hasattr(contact_1, 'get_contact'))
print(getattr(contact_1, 'get_contact'))
setattr(contact_1, 'get_contact', 'sent_message')
print(getattr(contact_1, 'get_contact'))
delattr(contact_1, 'get_contact')
print(getattr(contact_1, 'get_contact'))
print(getattr(contact_1, 'sent_message'))

print('   class UpdateContact')
print(hasattr(contact_2, 'job'))
print(getattr(contact_2, 'job'))
setattr(contact_2, 'job', 'CEO')
print(getattr(contact_2, 'job'))
delattr(contact_2, 'job')
print(hasattr(contact_2, 'get_message'))
print(getattr(contact_2, 'get_message'))
