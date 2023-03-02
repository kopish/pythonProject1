'''
sqlite3.Warning. Подкласс Exception. Его можно игнорировать, если нужно, чтобы оно не останавливало выполнение.
sqlite3.Error. Базовый класс для остальных исключений модуля sqlite3. Подкласс Exception.
sqlite3.DatabaseError. Исключение, которое возвращается при ошибках базы данных. Например, если попытаться открыть файл
как базу sqite3, хотя он ею не является, то вернется ошибка «sqlite3.DatabaseError: file is encrypted or is not a
database».
sqlite3.IntegrityError. Подкласс DatabaseError. Эта ошибка возвращается, когда затрагиваются отношения в базе,
например, например, не проходит проверка внешнего ключа.
sqlite3.ProgrammingError. Подкласс DatabaseError. Эта ошибка возникает из-за ошибок программиста: создание таблицы с
именем, которое уже занято, синтаксическая ошибка в SQL-запросах.
sqlite3.OperationalError. Подкласс DatabaseError. Эту ошибку невозможно контролировать. Она появляется в ситуациях,
которые касаются работы базы данных, например, обрыв соединения, неработающий сервер, проблемы с источником данных и
так далее.
sqlite3.NotSupportedError. Это исключение появляется при попытке использовать неподдерживаемое базой данных API.
Пример: вызов метода rollback() для соединения, которое не поддерживает транзакции. Вызов коммита после команды
создания таблицы.
Таким образом рекомендуется всегда писать код управления базой данных в блоке try, чтобы была возможность перехватывать
исключения и предпринимать действия, которые помогут справиться с ними.
'''

import sqlite3
import traceback
import sys

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")

    sqlite_insert_query = """INSERT INTO unknown_table_1
                          (id, text)  VALUES  (1, 'Демо текст')"""

    count = cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Не удалось вставить данные в таблицу sqlite")
    print("Класс исключения: ", error.__class__)
    print("Исключение", error.args)
    print("Печать подробноcтей исключения SQLite: ")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")