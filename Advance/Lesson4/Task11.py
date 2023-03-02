'''
В предыдущем примере для вставки одной записи в таблицу использовался метод execute() объекта cursor, но иногда
требуется вставить несколько строчек.

Например, при чтении файла, например, CSV, может потребоваться добавить все записи из него в таблицу SQLite. Вместе
выполнения запроса INSERT для каждой записи, можно выполнить все операции в один запрос. Добавить несколько записей в
таблицу SQLite можно с помощью метода executemany() объекта cursor.

Этот метод принимает два аргумента: запрос SQL и список записей.
'''

import sqlite3


def insert_multiple_records(records):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        # Инструкция SQLite INSERT содержит запрос с параметрами, где на месте каждого значения стоит
        # вопросительный знак.
        sqlite_insert_query = """INSERT INTO sqlitedb_developers
                                 (id, name, email, joining_date, salary)
                                 VALUES (?, ?, ?, ?, ?);"""
        # Дальше в таблицу вставляются несколько записей
        cursor.executemany(sqlite_insert_query, records)
        sqlite_connection.commit()
        # Количество вставленных строк используется метод cursor.rowcount.
        print("Записи успешно вставлены в таблицу sqlitedb_developers", cursor.rowcount)
        # Cохраняем изменения в БД
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


# После подключения к базе данных подготавливается список записей для вставки в таблицу.
# Каждая из них — это всего лишь строка.
records_to_insert = [(4, 'Jaroslav', 'idebylos@gmail.com', '2020-11-14', 8500),
                     (5, 'Timofei', 'ullegyddomm@gmail.com', '2020-11-15', 6600),
                     (6, 'Nikita', 'aqillysso@gmail.com', '2020-11-27', 7400)]

insert_multiple_records(records_to_insert)
