'''
Использование переменных в запросах для удаления строки
В большинстве случаев удалять строки из таблицы SQLite нужно с помощью ключа, который передается уже во время работы
программы. Например, когда пользователь удаляет свою подписку, запись о нем нужно удалить из таблицы.

В таких случаях требуется использовать запрос с параметрами. В таких запросах на месте будущих значений ставятся
заполнители (?). Это помогает удалять записи, получая значения во время работы программы, и избегать проблем
SQL-инъекций. Вот пример с удалением разработчика с id=5.
'''

import sqlite3


def delete_sqlite_record(dev_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """DELETE from sqlitedb_developers where id = ?"""
        cursor.execute(sql_update_query, (dev_id, ))
        sqlite_connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


delete_sqlite_record(5)

'''
Запрос с параметрами использовался, чтобы получить id разработчика во время работы программы и подставить его на 
место ?. Он определяет id записи, которая будет удалена.
После этого создается кортеж данных с помощью переменных Python.
Дальше DELETE-запрос вместе с данными передается в метод cursor.execute().
Наконец, изменения сохраняются в базе данных с помощью метода commit() класса Connection.
'''