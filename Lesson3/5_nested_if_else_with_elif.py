x = int(input('x = '))

# Заменим второй вложенный if в предыдущем примере
# на оператор ветвления с несколькими условиями
if 0 < x < 7:
    print('Значение x входит в заданный диапазон, продолжаем')
    y = 2 * x - 5

    if y < 0:
        print('Значение y отрицательно')
    elif y > 0:
        print('Значение y положительно')
    else:
        print('y = 0')
