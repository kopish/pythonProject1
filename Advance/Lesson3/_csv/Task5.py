'''
Для записи информации в CSV файл необходимо создать объект writer:

file_writer = csv.writer(w_file, delimiter = "\t")

Для записи в файл данных используется метод writerow(), который имеет следующий синтаксис:

writecol("Имя", "Фамилия", "Отчество")
'''
import csv

with open("data/file3.csv", mode="w", encoding='utf-8') as w_file:
    # lineterminator - разделитель между строками таблицы, по умолчанию он "\r\n".
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    # В качестве параметра метод writerow() принимает список, элементы которого будут записаны в строку через
    # символ-разделитель.
    file_writer.writerow(["Имя", "Класс", "Возраст"])
    file_writer.writerow(["Женя", "3", "10"])
    file_writer.writerow(["Саша", "5", "12"])
    file_writer.writerow(["Маша", "11", "18"])
