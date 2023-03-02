'''
Бывает такое, что есть несколько подключений к базе данных SQLite, и одно из них выполняет определенное изменение.
Для этого соединению требуется выполнить блокировку — база данных блокируется до тех пор, пока транзакция не будет
завершена.

Параметр timeout, который задается при подключении, определяет, как долго соединение будет ожидать отключения
блокировки перед возвращением исключения.

По умолчанию значение этого параметра равно 5.0 (5 секунд). Его не нужно задавать, потому что это значение по умолчанию.
Таким образом, при подключении к базе данных из Python, если ответ не будет получен в течение 5 секунд, вернется
исключение. Однако параметр все-таки можно задать в функции sqlite3.connect.
'''

import sqlite3


def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db', timeout=20)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT count(*) from sqlitedb_developers"""
        cursor.execute(sqlite_select_query)
        total_rows = cursor.fetchone()
        print("Всего строк:  ", total_rows)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


read_sqlite_table()
