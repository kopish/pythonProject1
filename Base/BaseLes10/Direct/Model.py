# расчёта площади
# # круга, квадрата, прямоугольника, треугольника и объёмов: шара, куба,
# # параллелепипеда и конуса.
import Mod

while True:
    geom = int(input("\nВиберіть дію.\n"
                     "1.Визначити площу кола\n"
                     "2.Визначити площу квадрату\n"
                     "3.Визначити площу трикутника\n"
                     "4.Визначити площу прямокутника\n"
                     "5.Визначити об'єм шара\n"
                     "6.Визначити об'єм куба\n"
                     "7.Визначити об'єм паралелепіпеду\n"
                     "8.Визначити об'єм конуса\n"
                     "0.Завершення\n\t"
                     "Оберіть дію: "))
    if geom == 1:
        r = int(input("Введіть радіус кола: "))
        result = Mod.s_circle(r)
    elif geom == 2:
        a = int(input("Введіть довжину сторони квадрату: "))
        result = Mod.s_square(r)
    elif geom == 3:
        a = int(input("Введіть довжину сторони 1: "))
        b = int(input("Введіть довжину сторони 2: "))
        result = Mod.s_rectangle(a, b)
    elif geom == 4:
        a = int(input("Введіть довжину катету 1: "))
        b = int(input("Введіть довжину катету 2: "))
        result = Mod.s_triangle(a, b)
    elif geom == 5:
        r = int(input("Введіть радіус: "))
        result = Mod.v_layer(r)
    elif geom == 6:
        a = int(input("Введіть довжину сторони: "))
        result = Mod.v_cube(a)
    elif geom == 7:
        a = int(input("Введіть довжину сторони 1: "))
        b = int(input("Введіть довжину сторони 2: "))
        c = int(input("Введіть висоту: "))
        result = Mod.v_paral(a, b, c)
    elif geom == 8:
        r = int(input("Введіть радіус основи конуса: "))
        h = int(input("Введіть висоту конуса: "))
        result = Mod.v_cone(r, h)
    elif geom == 0:
        break
    print(result)
