""" Урок 2, завдання 1
Створіть клас Editor, який містить методи view_document та edit_document. Нехай метод edit_document
виводить на екран інформацію про те, що редагування документів недоступне для безоплатної версії.
Створіть підклас ProEditor, у якому цей метод буде перевизначено. Введіть ліцензійний ключ із
клавіатури та, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor. Викличте методи
перегляду та редагування документів.
"""

CORRECT_LICENSE_KEY = '123'


class Editor:
    @staticmethod
    def view_document():
        print('You can view documents')

    def edit_document(self):
        print(f'{type(self)} : Documents editing is not possible in the free version')


class ProEditor(Editor):
    def edit_document(self):
        print(f'{type(self)} : You can edit documents in Pro version')


license_key = input('Enter the license key to edit documents: ')

print()
if license_key == CORRECT_LICENSE_KEY:
    doc_editor = ProEditor()
else:
    doc_editor = Editor()
doc_editor.view_document()
doc_editor.edit_document()
