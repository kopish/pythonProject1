a = 2
b = 5

# меньше
print(a < b)
# больше
print(b > 3)
# меньше или равно
print(a <= 2)
# больше или равно
print(b >= 7)
# двойное сравнение
print(a < 3 < b)
# равенство
print(a == b)
# неравенство
print(a != b)
# идентичность объектов в памяти
print(a is b)
# a и b – разные объекты (хотя значения их могуть быть равны)
print(a is not b)

string = "some string"
second_string = string
third_string = input('Введите строку: ')

print(string is second_string)
print(string is third_string)
