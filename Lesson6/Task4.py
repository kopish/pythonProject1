def function(a, b):
    if b == a:
        return b
    return b + function(a, b - 1)


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print(function(number1, number2))
