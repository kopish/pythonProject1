# Создайте программу-калькулятор, которая поддерживает четыре операции: сложение, вычитание, умножение, деление.
# Все данные должны вводиться в цикле, пока пользователь не укажет, что хочет завершить выполнение программы. Каждая
# операция должна быть реализована в виде отдельной функции. Функция деления должна проверять данные на корректность и
# выдавать сообщение об ошибке в случае попытки деления на ноль.
def addition(first, second):
    return first + second


def subtraction(first, second):
    return first - second


def multiplication(first, second):
    return first * second


def division(first, second):
    if second == 0:
        print("cannot be divided by zero")
    else:
        return first / second


operator = input("Click operation +, -, *, /, (Click 0 to finish): ")
while True:
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        num_1 = int(input("Enter the first number: "))
        num_2 = int(input("Enter the second number: "))
        if operator == "+":
            result = addition(num_1, num_2)
        elif operator == "-":
            result = subtraction(num_1, num_2)
        elif operator == "*":
            result = multiplication(num_1, num_2)
        elif operator == "/":
            result = division(num_1, num_2)
        elif operator == "0":
            break
        print("Result: ", result, "\n")
    operator = input("Click operation +, -, *, /, (Click 0 to finish): ")

