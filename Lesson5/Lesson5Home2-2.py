# Создайте две функции, вычисляющие значения определённых алгебраических выражений.
# Выведите на экран таблицу значений этих функций от -5 до 5 с шагом 0.5.

# Нажаль я зовсім не зрозумів завдання :(
def addition(y, x):
    return y + x


def subtraction(y, x):
    return y - x


num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
g = addition(num_1, num_2)
for i in range(10):
    print(g, end='  ')
    g -= 0.5
print()
for i in range(10):
    print(g, end='  ')
    g += 0.5
print()
f = subtraction(num_1, num_2)
for i in range(10):
    print(f, end='  ')
    f -= 0.5
print()
for i in range(10):
    print(f, end='  ')
    f += 0.5
print()
