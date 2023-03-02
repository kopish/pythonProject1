'''
---------------Создание или переопределение SQL-функций в SQLite---------------

В таких базах данных, как MySQL, MSSQL и PostgreSQL, есть возможность создавать функции и хранимые процедуры, но у
SQLite такой возможности нет. Таким образом, CREATE FUNCTION и CREATE PROCEDURE с этой базой данных работать не будут.
В этом материале рассмотрим, как создавать или переиспользовать SQL-функции из Python.

C API базы данных SQLite дает возможность создавать пользовательские функции или переопределять поведение существующих.
Модуль sqlite3 — это всего лишь оболочка для этого C API, которая предоставляет возможность создавать или переопределять
SQLite-функции из Python.

В определенных случаях возникает необходимость совершать определенные вещи при выполнении SQL-запроса, особенно, если
это обновление или получение данных. В таких случаях на помощь приходят пользовательские функции. Например, при
получении имени пользователя нужно, чтобы оно вернулось в верхнем регистре.

В SQLite есть масса встроенных функций: LENGTH, LOWER, UPPER, SUBSTR, REPLACE и другие. Добавим к этому списку TOTITLE
для конвертации любой строки и в строку с заглавными буквами.

Функция принимает три аргумента:

name — имя функции
num_params — количество параметров, которые функция принимает
func — функция Python, которая вызывается внутри запроса
Эта функция создает пользовательскую функцию, которую можно использовать в инструкциях SQL, ссылаясь на ее name.

Примечание: если в качестве параметра num_params передать значение -1, то функция будет принимать любое количество
аргументов. connection.create_function() может возвращать любые типы, поддерживаемые SQLite: bytes, str, int, float и
None.

Создадим новую функцию в SQLite с помощью connection.create_function().
'''

import sqlite3

# Принимает строку в качестве входящего значения и конвертирует ее в строку с заглавными буквами
def _to_title_case(string):
    return str(string).title()


def get_developer_name(dev_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        # После этого вызывается create_function из класса connection. В нее передаются три аргумента: название функции,
        # количество параметров, которые будет принимать _to_title_case и функция Python, которая будет вызываться как
        # SQL-функция.
        # После этого функция TOTITLECASE вызывается в запросе SELECT для получения имени разработчика в виде строки с
        # заглавными буквами
        sqlite_connection.create_function("TOTILECASE", 1, _to_title_case)
        select_query = "SELECT TOTILECASE(name) FROM sqlitedb_developers where id = ?"
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


get_developer_name(2)
