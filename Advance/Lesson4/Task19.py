'''
Обновление нескольких колонок таблицы SQLite
Можно обновить несколько колонок таблицы SQLite в один запрос. Для этого нужно лишь подготовить запрос с параметрами
и заполнителями.
'''

import sqlite3


def update_multiple_columns(dev_id, salary, email):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_update_query = """Update sqlitedb_developers set salary = ?, email = ? where id = ?"""
        column_values = (salary, email, dev_id)
        cursor.execute(sqlite_update_query, column_values)
        sqlite_connection.commit()
        print("Несколько столбцов успешно обновлены")
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


update_multiple_columns(3, 2500, 'bec9988@gmail.com')