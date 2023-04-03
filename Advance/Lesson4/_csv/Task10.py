'''
Чтение в pandas
В библиотеке для анализа данных pandas так же есть возможность прочитать CSV файл. Эта библиотека устанавливается
отдельно:
'''

import pandas

csv = pandas.read_csv('data/file.csv', delimiter=';')
print(csv)