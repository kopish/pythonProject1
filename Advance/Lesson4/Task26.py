'''
---------------Получение изображения и файла, сохраненных в виде BLOB-------------

Предположим, данные, которые хранятся в виде BLOB в базе данных, нужно получить, записать в файл на диске и открыть в
привычном виде. Как это делается?

Для этого нужно проделать следующие шаги:

* Установить SQLite-соединение с базой данных из Python;
* Создать объект cursor из объекта соединения;
* Создать SELECT-запрос для получения BLOB-колонок из таблицы;
* Использовать cursor.fetchall() для получения всех строк и перебора по ним;
* Создать функцию для конвертации BLOB-данных в нужный формат и записать готовые файлы на диск;
* Закрыть объект cursor и соединение.
'''

import sqlite3, os


def write_to_file(data, filename):
    # Преобразование двоичных данных в нужный формат
    with open(filename, 'wb') as file:
        file.write(data)
    print("Данный из blob сохранены в: ", filename, "\n")


def read_blob_data(emp_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[2]
            resume_file = row[3]

            print("Сохранение изображения сотрудника и резюме на диске \n")
            photo_path = os.path.join("db_data", name + ".jpg")
            resume_path = os.path.join("db_data", name + "_resume.txt")
            write_to_file(photo, photo_path)
            write_to_file(resume_file, resume_path)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


read_blob_data(1)
read_blob_data(2)

'''
Изображения и файлы действительно сохранились на диске.

Получение изображения и файла, сохраненных в виде BLOB
Примечание: для копирования бинарных данных на диск они сперва должны быть конвертированы в нужный формат. 
В этом примере форматами были .jpg и .txt.
'''