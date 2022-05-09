# Создайте программу, которая рисует на экране прямоугольник
# из звёздочек заданной пользователем ширины и высоты.
num1 = int(input("Enter the number of lines: "))
num2 = int(input("Enter the number of vertical lines: "))
for i in range(num1):
    for j in range(num2):
        print("*", end='')
        print(" ", end='')
    print()