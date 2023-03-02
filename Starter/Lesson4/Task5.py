password = input('Введите пароль: ').lower()
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for symbol in password:
    print(alphabet.find(symbol) + 1)
