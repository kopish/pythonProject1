# Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print()
# выведите на экран прямоугольный треугольник.
num = 5
for i in range(5):
    for j in range(num):
        print('*', end='')
        print(' ', end='')
    num -= 1
    print()
