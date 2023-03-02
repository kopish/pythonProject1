# Подключаем нужные модули:
from turtle import *

# Создаём объекты типа "Черепашка" и запоминаем их в переменных
# Устанавливаем нужные свойства черепашек:
# цвет, скорость, форма, место, "перо" поднимается и опускается
t1 = Turtle()
t1.color('red')
t1.speed(10)
t1.shape('triangle')
t1.left(30)
t1.penup()
t1.goto(-50, 50)
t1.pendown()

# Все то же для черепашки 2
t2 = Turtle()
t2.color('blue')
t2.speed(10)
t2.shape('circle')
t2.left(150)
t2.penup()
t2.goto(-50, -50)
t2.pendown()

# Все то же для черепашки 3
t3 = Turtle()
t3.color('green')
t3.speed(10)
t3.shape('turtle')
t3.left(180)
t3.penup()
t3.goto(50, 50)
t3.pendown()

# Все то же для черепашки 4
t4 = Turtle()
t4.color('orange')
t4.speed(10)
t4.shape('square')
t4.left(270)
t4.penup()
t4.goto(50, -50)
t4.pendown()

# Установка направления: все черепашки смотрят вправо:
t1.seth(0)
t2.seth(0)
t3.seth(0)
t4.seth(0)

# Основной цикл: повторяется движение вперёд и влево:
i = 1
while i < 30:
    t1.forward(2 * i)
    t1.left(90)
    t2.forward(2 * i)
    t2.left(90)
    t3.forward(2 * i)
    t3.left(90)
    t4.forward(2 * i)
    t4.left(90)
    i = i + 1

# Задерживаем картинку на экране
exitonclick()
