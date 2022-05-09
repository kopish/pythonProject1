category = input('Введите категорию товара: ')
wish = input('Введите предпочтение: ')
if category == 'молочные продукты':
    if wish == 'фермерское':
        print('Экоферма')
    else:
        print('Моя ферма')
if category == 'хлеб':
    if wish == 'домашний':
        print('Паляница')
    else:
        print('Турецкий')
