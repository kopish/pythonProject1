while True:
    try:
        a = int(input('Сторона квадрата:'))
        break
    except:
        print('Ошибка! Введите число без других символов')
    finally:
        print('Вот это задача!')
print('Периметр квадрата:', a * 4)
