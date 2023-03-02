'''
Обычно при выполнении запроса на вставку объекта datetime модуль sqlite3 в Python конвертирует его в строковый формат.
То же самое происходит при получении данных из таблицы — они возвращаются в строковом формате.
'''

import sqlite3


def read_sqlite_table(records):
    try:
        # Установка соединения с БД
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        # Получение объекта Cursor из объекта соединения
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        # Подготовка SELECT-запроса для получения всех строк из таблицы sqlitedb_developers. Она содержит пять колонок.
        sqlite_select_query = """SELECT * from sqlitedb_developers"""
        cursor.execute(sqlite_select_query)
        # После успешного выполнения запроса используется метод cursor.fetchall() для получения всех(cursor.fetchone()
        # — для одной строки / cursor.fetchmany(SIZE) — для ограниченного количества строк) записей таблицы
        # sqlitedb_developers.
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        # Перебор всех записей и вывода их по одному
        for row in records:
            print("ID:", row[0])
            print("Имя:", row[1])
            print("Почта:", row[2])
            print("Добавлен:", row[3])
            print("Зарплата:", row[4], end="\n\n")
        # объект Cursor закрывается
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        # Закрітие соединения с БД
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


read_sqlite_table(1)

'''
В этом примере прямо отображаются строка и значение ее колонки. Если вам нужно использовать значения колонки в своей 
программе, то их можно сохранять в переменные Python. Для этого нужно написать, например, так: name = row[1]
'''