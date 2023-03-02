'''
----------------------Операция Delete для удаления нескольких строк--------------------------

Часто приходится удалять сразу несколько одновременно.
Вместо выполнения запроса DELETE каждый раз для каждой записи, можно выполнить операцию массового удаления в одном
запросе. Удалить несколько записей из SQLite-таблицы в один запрос можно с помощью метода cursor.executemany().
Метод cursor.executemany(query, seq_param) принимает два аргумента: SQL-запрос и список записей для удаления.
'''
import sqlite3


def delete_multiple_records(ids_list):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_update_query = """DELETE from sqlitedb_developers where id = ?"""
        cursor.executemany(sqlite_update_query, ids_list)
        sqlite_connection.commit()
        print("Удалено записей:", cursor.rowcount)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


ids_to_delete = [(4,),(3,)]
delete_multiple_records(ids_to_delete)

'''
После соединения с базой данных SQLite готовится SQL-запрос с параметрами и одним заполнителем. Вместе с ним также 
передается список id в формате кортежа.
Каждый элемент списка — это всего лишь кортеж каждой строки. Каждый кортеж содержит id разработчика. В этом примере 
три кортежа — то есть, три разработчика.
Дальше вызывается cursor.executemany(sqlite_delete_query, ids_list) для удаления нескольких записей из таблицы. И 
запрос, и список id передаются cursor.executemany() в качестве аргументов.
Чтобы увидеть количество затронутых записей, можно использовать метод cursor.rowcount. Наконец, изменения сохраняются 
в базу данных с помощью метода commit класса Connection.
'''