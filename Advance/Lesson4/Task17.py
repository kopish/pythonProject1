'''
Использование переменных Python в запросе UPDATE
Большую часть времени обновление таблицы нужно выполнять с помощью значений, получаемых при работе программы. Например,
когда пользователи обновляют свой профиль через графический интерфейс, нужно обновить заданные ими значения в
соответствующей таблице.

В таком случае рекомендуется использовать запрос с параметрами. Такие запросы используют заполнители (?) прямо внутри
инструкций SQL. Это помогает обновлять значения с помощью переменных, а также предотвращать SQL-инъекции.
'''

import sqlite3


def update_sqlite_table(dev_id, salary):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update sqlitedb_developers set salary = ? where id = ?"""
        data = (salary, dev_id)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


update_sqlite_table(3, 7500)

'''
Запрос с параметрами был использован для того, чтобы получить значения при работе программы и установить их на места 
заполнителей. В этом случае один из них отвечает за колонку «salary», а второй – колонку id.
После этого готовится кортеж с данными из двух переменных Python в определенном порядке. Этот кортеж вместе с запросом 
передается в метод cursor.execute(). Важно помнить, что в данном случае порядок переменных в кортеже играет значение.
В конце изменения закрепляются с помощью метода commit класса connection.
'''