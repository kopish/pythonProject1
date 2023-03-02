my_file = open("some.txt", "w")
print("Имя файла:", my_file.name)
print("Файл закрыт:", my_file.closed)
print("В каком режиме файл открыт:", my_file.mode)
# в скольких байтах от начала файла мы сейчас находимся:
print("Текущая позиция указателя чтения/записи в файле(в байтах):", my_file.tell)
print("Текущая позиция указателя чтения/записи в файле(в байтах):", my_file.tell())
my_file.close()
print("Файл закрыт:", my_file.closed)

