# Простым называется число, которое делится нацело только на единицу и само себя.
# Число 1 не считается простым. Напишите программу, которая находит все простые числа в заданном промежутке,
# выводит их на экран, а затем по требованию пользователя выводит их сумму либо произведение.
my_list = []
value1 = int(input("Введите первое значение: "))
value2 = int(input("Введите второе значение: "))

for element in range(value1, value2 + 1):
    if value1 <= 1 and value2 <= 1:
        print("Нет простых чисел")
    if value1 <= 2:
        value1 = 2
    if value1 <= value2:
        my_list.append(value1)
    value1 += 1
print(my_list)
print()

operator = input("Выберите операцию с простыми числами \n1. Сумма\n2. Произведение\n")


def multiplication(a):
    if a:
        return a[0] * multiplication(a[1:])
    return 1


if operator == "1" or operator == "2":
    if operator == "1":
        result = sum(my_list)
    elif operator == "2":
        result = multiplication(my_list)
    print("Result: ", result, "\n")
