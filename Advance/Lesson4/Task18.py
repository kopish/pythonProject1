'''
-----------------Обновление нескольких строк SQLite-таблицы------------------------

В последнем примере использовался метод execute() объекта cursor для обновления одного значения, но иногда в
приложениях Python нужно обновить несколько строк. Например, нужно увеличить зарплату большинства разработчиков на 20%.
Вместе выполнения операции UPDATE каждый раз для каждой записи можно выполнить массовое обновление в один запрос.
Изменить несколько записей в таблице SQLite в один запрос можно с помощью метода cursor.executemany().

Метод cursor.executemany(query, seq_param) принимает два аргумента: SQL-запрос и список записей для обновления.
'''

import sqlite3


def update_multiple_records(record_list):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_update_query = """Update sqlitedb_developers set salary = ? where id = ?"""
        cursor.executemany(sqlite_update_query, record_list)
        sqlite_connection.commit()
        print("Записей", cursor.rowcount, ". Успешно обновлены")
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


records_to_update = [(9700, 4), (7800, 5), (8400, 6)]
update_multiple_records(records_to_update)

'''
После подключения к таблице SQLite готовится SQLite-запрос с двумя заполнителями (колонки salary и id), а также список 
записей для обновления в формате кортежа.
Каждый элемент – это кортеж для каждой записи. Каждый кортеж содержит два значения: зарплату и id разработчика.
Функция cursor.executemany(sqlite_update_query, record_list) вызывается для обновления нескольких строк таблицы SQLite.
Чтобы узнать, какое количество записей было изменено, используется функция cursor.rowcount. Наконец, данные сохраняются 
в базу данных с помощью метода commit класса connection
'''