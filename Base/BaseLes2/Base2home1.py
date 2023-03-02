# Создайте класс Editor, который содержит методы view_document и edit_document.
# Пусть метод edit_document выводит на экран информацию о том, что
# редактирование документов недоступно для бесплатной версии. Создайте подкласс
# ProEditor, в котором данный метод будет переопределён. Введите с клавиатуры
# лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor
# иначе Editor. Вызовите методы просмотра и редактирования документов.
class Editor:
    def __init__(self, document='Empty Document'):
        self.document = document

    def view_document(self):
        return self.document

    def edit_document(self):
        print('In the free version, editing access is prohibited.')
        print(Editor.view_document(self))
        ProEditor.edit_document(self)


class ProEditor(Editor):
    def view_document(self):
            print('Write down the new version of doc')
            new_ver = input()
            self.document = new_ver
            print('Document changed:')
            print(self.document)
            ProEditor.edit_document(self)

    def edit_document(self):
        password = input('Enter password to achieve pro features: ')
        if password == 'pro':
            ProEditor.view_document(self)
        else:
            Editor.view_document(self)
            Editor.edit_document(self)


ed1 = ProEditor()
ed1.edit_document()