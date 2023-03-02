'''
Вставка/получение объекта DateTime
Обычно при выполнении запроса на вставку объекта datetime модуль sqlite3 в Python конвертирует его в строковый формат.
То же самое происходит при получении данных из таблицы — они возвращаются в строковом формате.
'''

import sqlite3, datetime


def add_developer(dev_id, name, joining_date):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_create_table_query = '''CREATE TABLE new_developers (
                                       id INTEGER PRIMARY KEY,
                                       name TEXT NOT NULL,
                                       joiningDate timestamp);'''

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)

        # вставить данные разработчика
        sqlite_insert_with_param = """INSERT INTO 'new_developers'
                          ('id', 'name', 'joiningDate')
                          VALUES (?, ?, ?);"""

        data_tuple = (dev_id, name, joining_date)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Разработчик успешно добавлен \n")

        # получить данные разработчика
        sqlite_select_query = """SELECT name, joiningDate from new_developers where id = ?"""
        cursor.execute(sqlite_select_query, (1,))
        records = cursor.fetchall()

        for row in records:
            developer= row[0]
            joining_date = row[1]
            print(developer, "присоединился", joining_date)
            print("тип даты", type(joining_date))
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


add_developer(1, 'Mark', datetime.datetime.now())

'''
Как можно видеть, в таблицу был вставлен объект даты, но после получения он стал строкой. Однако это не мешает 
конвертировать результат обратно в объект даты.
Для этого используется detect_types с PARSE_DECLTYPES и PARSE_COLNAMES в качестве аргументов в методе connect модуля 
sqlite3.

sqlite3.PARSE_DECLTYPES

Эта константа используется как значение параметра detect_types метода connect().
Если использовать этот параметр в методе connect(), то модуль sqlite3 будет парсить тип каждой получаемой колонки.

После парсинга используется словарь конвертации типов для поиска выполнения конкретной функции конвертации.

sqlite3.PARSE_COLNAMES

Эта константа нужна для того же параметра.
При ее использовании интерфейс SQLite сохранит значения имени каждой возвращаемой колонки. После этого можно аналогично
использовать словарь для конвертации в нужный тип.
'''