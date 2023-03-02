import math


def circle(radius):
    return 2 * math.pi * radius


while True:
    try:
        rad = int(input("Введите радиус: "))
        if rad <= 0:
            print("Значение должно быть положительное")
        else:
            break
    except ValueError:
        print("Значение должно быть целочисленное")

print(circle(rad))
