import csv

with open('data/file7.csv', 'r') as f:
    # читаем первые 100 символов (или весь файл)
    sample = f.read(20)
    # пример проверки, что файл имеет заголовки
    header = csv.Sniffer().has_header(sample)
    print('В файле есть заголовки: ', header)
    # создаем диалект
    dialect = csv.Sniffer().sniff(sample)

with open('data/file7.csv', 'r') as f:
    # передаем диалект и читаем файл
    reader = csv.reader(f, dialect)
    for row in reader:
        print(row)