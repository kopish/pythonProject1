# Опишите классы графического объекта, прямоугольника и объекта, который может
# обрабатывать нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и
# обычного прямоугольника. Вызовите метод нажатия на кнопку.
class Figure:
    def __init__(self, side1=10, side2=15):
        self.side1 = side1
        self.side2 = side2


class Rectangle(Figure):
    def square(self):
        for i in range(self.side1):
            print("** " * self.side2)


class Object(Rectangle, Figure):
    def mouse(self):
        text = input("Turn on a mouse button: ")
        print("You turn on a program!!!", text)


que = Object(5, 5)
que.square()
que.mouse()


