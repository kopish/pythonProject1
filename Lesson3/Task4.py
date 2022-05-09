height = float(input('Введите ваш рост: '))
weight = float(input('Введите ваш вес: '))

if height - weight > 100:
    print('Ваш вес в норме.')
else:
    print('Ваш вес в опасности=).')
