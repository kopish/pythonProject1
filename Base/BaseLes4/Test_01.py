a = input('Введите длину первой стороны:')
try:
    a = int(a)
except:
    print('Ошибка! Введите длину целым числом без букв')
    a = int(input('Введите длину первой стороны:'))
b = input('Введите длину второй стороны:')
try:
    b = int(b)
except:
    print('Ошибка! Введите длину целым числом без букв')
    b = int(input('Введите длину второй стороны:'))
s = a * b
print('Площадь прямоугольника:', s)
