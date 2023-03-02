# Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно).
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
x = a
y = 0
while a <= x <= b:
    y += x
    x += 1

print(y)