'''
Сейчас таблица sqlitedb_developers содержит шесть строк, а удалять будем разработчика, чей id равен 6. Вот что для
этого нужно сделать:

Присоединиться к SQLite из Python;
Создать объект Cursor с помощью полученного в прошлом шаге объекта соединения SQLite;
Создать DELETE-запрос для SQLite. Именно на этом этапе нужно знать названия таблицы и колонок;
Выполнить DELETE-запрос с помощью cursor.execute();
После выполнения запроса необходимо закоммитить изменения в базу данных;
Закрыть соединение с базой данных;
Также важно не забыть перехватить исключения, которые могут возникнуть;
Наконец, проверить результат операции.
'''

import sqlite3


def delete_record():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_delete_query = """DELETE from sqlitedb_developers where id = 6"""
        cursor.execute(sql_delete_query)
        sqlite_connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


delete_record()

'''
Примечание: если выполняется несколько операций удаления, и есть необходимость отменить все изменения в случае неудачи 
хотя бы с одной из них, нужно использовать функцию rollback() класса соединения для отмены. Эту функцию стоит применять 
внутри блока except.
'''