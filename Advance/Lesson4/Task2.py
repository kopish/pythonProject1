# Создание таблицы — это DDL-запрос, выполняемый из Python
# Cоздадим базу sqlitedb_developers в базе данных sqlite_python.db

import sqlite3

try:
    # Соединяемся с БД
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    # Подготавливаем запрос создания таблицы
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS sqlitedb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                joining_date datetime,
                                salary REAL NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    # Выполняем запрос с помощью cursor.execute(query)
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")
    # Закрываем соединение с базой и объектом cursor
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

'''
Перед переходом к выполнению CRUD-операций в SQLite из Python сначала нужно разобраться с типами данных SQLite и 
соответствующими им типами данных в Python, которые помогают хранить и считывать данные из таблицы.
У движка SQLite есть несколько классов для хранения значений. Каждое значение, хранящееся в базе данных, имеет один из
следующих типов или классов.

NULL — значение NULL
INTEGER — числовые значения. Целые числа хранятся в 1, 2, 3, 4, 6 и 8 байтах в зависимости от величины
REAL — числа с плавающей точкой, например, 3.14, число Пи
TEXT — текстовые значения. Могут храниться в кодировке UTF-8, UTF-16BE или UTF-16LE
BLOB — бинарные данные. Для хранения изображений и файлов
Следующие типы данных из Python без проблем конвертируются в SQLite. Для конвертации достаточно лишь запомнить эту таблицу.

Тип Python - Тип SQLite
None - NULL
int - INTEGER
float - REAL
str	- TEXT
bytes - BLOB
'''

