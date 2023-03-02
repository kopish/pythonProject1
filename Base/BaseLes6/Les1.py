# Последовательность, список 5-25, значение на екран в пятую степень
print([x ** 5 for x in range(5, 26)])
x = (i ** 5 for i in range(5, 26))
while True:
    try:
        print(next(x))
    except StopIteration:
        break
