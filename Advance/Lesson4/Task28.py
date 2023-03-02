'''
При считывании объекта datetime из таблицы SQLite нужно получить объединяющий тип — datetime.
'''

import sqlite3, datetime


def add_developer(dev_id, name, joining_date):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db',
                                            detect_types=sqlite3.PARSE_DECLTYPES |
                                            sqlite3.PARSE_COLNAMES)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_create_table_query = '''CREATE TABLE new_developers2 (
                                       id INTEGER PRIMARY KEY,
                                       name TEXT NOT NULL,
                                       joiningDate timestamp);'''

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)

        # вставить данные разработчика
        sqlite_insert_with_param = """INSERT INTO 'new_developers2'
                          ('id', 'name', 'joiningDate')
                          VALUES (?, ?, ?);"""

        data_tuple = (dev_id, name, joining_date)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Разработчик успешно добавлен \n")

        # получить данные разработчика
        sqlite_select_query = """SELECT name, joiningDate from new_developers2 where id = ?"""
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
# В результате вернувшиеся данные из таблицы представлены типом datetime.datetime.