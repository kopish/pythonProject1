'''
Дополнительные параметры DictWriter
Объект writer также имеет атрибут dialect, который определяет, как будут форматироваться данные при записи в файл, про него будет описано ниже.

Кроме того, writer имеет методы:

writerows(rows) — Записывает все элементы строк.
writeheader() — Выводит заголовки для столбцов. Заголовки должны быть переданы объекту writer в виде списка, как атрибут fieldnames.
writeheader был использован в предыдущем примере. Рассмотрим применение writerows:
'''

import csv

with open("data/file5.csv", mode="w", encoding='utf-8') as w_file:
    names = ["Имя", "Возраст"]
    file_writer = csv.DictWriter(w_file, delimiter=",",
                                 lineterminator="\r", fieldnames=names)
    file_writer.writerows([{"Имя": "Саша", "Возраст": "6"},
                           {"Имя": "Маша", "Возраст": "15"},
                           {"Имя": "Вова", "Возраст": "14"}])


