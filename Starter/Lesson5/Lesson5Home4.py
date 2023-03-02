# Создайте программу, которая состоит из функции, которая принимает три числа и возвращает их среднее арифметическое,
# и главного цикла, спрашивающего у пользователя числа и вычисляющего их средние значения при помощи созданной функции.
def arithmetic_mean():
    return (first + second + third) / 3


while True:
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    third = int(input("Enter the third number: "))
    print("Arithmetic mean: ", round(arithmetic_mean(), 2), "\n")
