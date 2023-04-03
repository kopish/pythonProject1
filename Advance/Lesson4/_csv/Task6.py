'''
Запись в файл также может быть осуществлена с помощью объекта DictWriter. Важно помнить, что он требует явного указания
параметра fieldnames. В качестве аргумента метода writerow используется словарь.

Код программы выглядит так:
'''
import csv

with open("data/file4.csv", mode="w", encoding='utf-8') as w_file:
    names = ["Имя", "Возраст"]
    file_writer = csv.DictWriter(w_file, delimiter=",",
                                 lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
    file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
    file_writer.writerow({"Имя": "Вова", "Возраст": "14"})
