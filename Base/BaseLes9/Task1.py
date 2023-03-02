# Режимы работы с файлами
file = open("test.txt", "r")  # чтение файла
file = open("test.txt", "w")  # запись файла, в слуаче отсутствия файла, его создание, а в случае наличия - обрезка
file = open("test.txt", "a")  # дозапись файла, в слуаче отсутствия файла, его создание
file = open("test2.txt", "x")  # открытие файла для его эксклюзивного создания, если файл существует, операция не
# выполняется
file = open("test2.txt", "rb")  # открытие файла в бинарном режиме
file = open("test2.txt", "rt")  # открытие файла в текстовом режиме (по умолчанию)
file = open("test2.txt", "r+")  # открытие файла для обновления (чтения и записи)

file = open("image.bmp", 'w+b')  # чтение и запись файла в двоичном режиме

file.close()
