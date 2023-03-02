'''
Переопределение существующих функций SQLite
Иногда нужно переопределить уже существующие функции. Например, при возвращении имени пользователя необходимо, чтобы
оно было в верхнем регистре.
В качестве демонстрации конвертируем встроенную в SQLite функцию LOWER в UPPER, чтобы при ее вызове она превращала
входящие данные в верхний регистр.
Создадим новое определение для функции lower() с помощью метода connection.create_function(). Таким образом мы
перезаписываем уже существующую реализацию функции lower().
'''
import sqlite3


def lower(string):
    return str(string).upper()


def get_developer_name(dev_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_connection.create_function("lower", 1, lower)
        select_query = "SELECT lower(name) FROM sqlitedb_developers where id = ?"
        cursor.execute(select_query, (dev_id,))
        name = cursor.fetchone()
        print("Имя разработчика", name)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


get_developer_name(1)