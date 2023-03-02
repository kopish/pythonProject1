'''
Сейчас таблица sqlitedb_developers содержит шесть строк, поэтому обновим зарплату разработчика с id 4. Для выполнения запроса UPDATE из Python нужно выполнить следующие шаги:

Сперва нужно установить SQLite-соединение из Python.
Дальше необходимо создать объект cursor с помощью объекта соединения.
После этого – создать запрос UPDATE. Для этого нужно знать названия таблицы и колонки, которую потребуется обновить.
Дальше запрос выполняется с помощью cursor.execute().
После успешного завершения запроса нужно не забыть закоммитить изменения в базу данных.
Соединение с базой данных закрывается.
Также важно не забыть перехватывать все исключения SQLite.
Наконец, нужно убедиться, что операция прошло успешно, получив данные из таблицы.
'''

import sqlite3


def update_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update sqlitedb_developers set salary = 10000 where id = 4"""
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

update_sqlite_table()

# Примечание: если выполняется операция массового обновления и есть необходимость откатить изменения в случае ошибки
# хотя бы при одном, нужно использовать функцию rollback() класса connection. Ее необходимо применить в блоке except