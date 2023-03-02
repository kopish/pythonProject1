my_shelf = dict()
author = input('Введите автора (q - завершить):')
while author != 'q':
    books = list()
    book = input('Введите книгу (s - стоп):')
    while book != 's':
        books.append(book)
        book = input('Введите книгу (s - стоп):')
    my_shelf[author] = books
    author = input('Введите автора (q - завершить):')

for author in my_shelf:
    print(author, '-', my_shelf[author])
