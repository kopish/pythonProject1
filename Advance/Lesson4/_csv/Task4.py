'''
Дополнительные параметры объекта DictReader
DictReader имеет параметры:

dialect — Набор параметров для форматирования информации. Подробнее про них ниже.
line_num — Устанавливает количество строк, которое может быть прочитано.
fieldnames — Определяет заголовки для столбцов, если не определить атрибут, то в него запишутся элементы из первой
прочитанной строки файла. Заголовки нужны для того, чтобы легко было понять, какая информация содержится или должна
содержаться в столбце.
Например, если бы в classmates.csv не было бы первой строки с заголовками, то можно было бы его открыть следующим
образом:
'''
fieldnames = ['Имя', 'Успеваемость', 'Год рождения']
file_reader = csv.DictReader(r_file, fieldnames = fieldnames)
'''Также можно использовать метод __next__() для получения следующей строки. Этот метод делает объект reader итерируемым.
То есть он вызывается при каждой итерации и возвращает следующую строку. Этот метод и используется при каждой итерации
в цикле for для получения очередной строки.
'''
