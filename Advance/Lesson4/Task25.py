'''
Работа с изображениями и файлами в SQLite

В качестве бинарных данных могут выступать файлы с любым расширением, изображения, видео или другие медиа;
BLOB-данные можно считывать из таблицы SQLite.
Перед выполнением операций над BLOB-данными убедитесь, что вы знаете название таблицы SQLite. Для хранения этой
информации нужно или создать новую, или изменить существующую, добавив колонку соответствующего типа.

В этом примере будет использоваться таблица new_employee. Ее можно создать с помощью следующего скрипта:

CREATE TABLE new_employee (id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL);
Эта таблица содержит две BLOB-колонки:

Колонка photo для хранения изображения сотрудника.
Колонка resume для хранения файла резюме.
Но стоит также разобраться с тем, что же такое BLOB.

BLOB (large binary object — «большой бинарный объект») — это тип данных, который используется для хранения «тяжелых»
файлов, таких как изображения, видео, музыка, документы и так далее. Перед сохранением в базе данных эти файлы нужно
конвертировать в бинарные данные — то есть, массив байтов.

Вставка изображений и файлов в таблицу
Вставим изображение и резюме сотрудника в таблицу new_employee. Для этого требуется выполнить следующие шаги:

Установить SQLite-соединение с базой данных из Python;
Создать объект cursor из объекта соединения;
Создать INSERT-запрос. На этом этапе нужно знать названия таблицы и колонки, в которую будет выполняться вставка;
Создать функцию для конвертации цифровых данных (например, изображений или файлов) в бинарные;
Выполнить INSERT-запрос с помощью cursor.execute();
После успешного завершения операции закоммитить сохранения в базу данных;
Закрыть объект cursor и соединение;
Перехватить любые SQL-исключения.
'''
import sqlite3


def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def insert_blob(emp_id, name, photo, resume_file):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_blob_query = """INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        emp_photo = convert_to_binary_data(photo)
        resume = convert_to_binary_data(resume_file)
        # Преобразование данных в формат кортежа
        data_tuple = (emp_id, name, emp_photo, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Изображение и файл успешно вставлены как BLOB в таблиу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


insert_blob(1, "Smith", "smith.jpg", "smith_resume.docx")
insert_blob(2, "David", "david.jpg", "david_resume.docx")

'''
В примере были вставлены id сотрудника, имя, фото и файл с резюме. Для последних двух были переданы местоположения 
файлов, так что программа смогла считать их и конвертировать в бинарные данные
Как можно явно увидеть, изображение и файл конвертировались в бинарный формат в процессе чтения данных в режиме rb. И 
только после этого данные были вставлены в колонку BLOB. Также был использован запрос с параметрами для вставки 
динамических данных в таблицу.
'''