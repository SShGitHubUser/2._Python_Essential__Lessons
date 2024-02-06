""" Урок 5, завдання 4
Використовуючи код з завдання 2, створити 2 екземпляри обох класів. Використати функції isinstance() –
для перевірки екземплярів класу (за яким класом створені) та issubclass() – для перевірки та визначення
класу-нащадка.
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

print(f' 1. {isinstance(contact_1, Contact)}')
print(f' 2. {isinstance(contact_2, Contact)}')
print(f' 3. {isinstance(contact_1, UpdateContact)}')
print(f' 4. {isinstance(contact_2, UpdateContact)}')
print(f' 5. {issubclass(UpdateContact, Contact)}')
print(f' 6. {issubclass(Contact, UpdateContact)}')
print(f' 7. {issubclass(Contact, Contact)}')
print(f' 8. {issubclass(UpdateContact, UpdateContact)}')
print(f' 9. {issubclass(Contact, object)}')
print(f'10. {issubclass(UpdateContact, object)}')
