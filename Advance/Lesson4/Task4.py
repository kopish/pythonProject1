# Выполнение SQL запросов с помощью функции executescript
'''
Скрипты SQLite отлично справляются со стандартными задачами. Это набор SQL-команд, сохраненных в файле (в формате .sql).
Один файл содержит одну или больше SQL-операций, которые затем выполняются из командной строки.

Дальше несколько распространенных сценариев использования SQL-скриптов

Создание резервных копий сразу нескольких баз данных за раз.
Сравнение количества строк двух разных баз с одной схемой.
Создание всех таблиц в одном скрипте, что позволит создать нужную схему на любом сервере
Выполнить скрипт из командной строки SQLite можно с помощью команды .read:

sqlite> .read sqlitescript.sql

CREATE TABLE fruits (
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 price REAL NOT NULL
);

CREATE TABLE drinks (
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 price REAL NOT NULL
);
'''

# Тоже самое на Python:
import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")

    with open('sqlite_examples.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()

    cursor.executescript(sql_script)
    print("Скрипт SQLite успешно выполнен")
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")