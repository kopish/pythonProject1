'''
Получение одной строки из таблицы
Когда нужно получить одну строку из таблицы SQLite, стоит использовать метод fetchone() класса cursor. Этот метод
необходим в тех случаях, когда известно, что запрос вернет одну строку.

cursor.fetchone() получает только следующую строку из результата. Если же строк нет, то возвращается None.
'''

import sqlite3


def read_single_row(developer_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from sqlitedb_developers where id = ?"""
        cursor.execute(sqlite_select_query, (developer_id, ))
        print("Чтение одной строки \n")
        record = cursor.fetchone()
        print("ID:", record[0])
        print("Имя:", record[1])
        print("Почта:", record[2])
        print("Добавлен:", record[3])
        print("Зарплата:", record[4])

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


read_single_row(3)