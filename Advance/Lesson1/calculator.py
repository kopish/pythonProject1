

operation = {}
while True:
    operation = input('Введите знак арифметической операции: ')
    x = float(input('Введите первое число: '))
    y = float(input('Введите второе число: '))
    result = None
    if operation == '+':
        result = lambda x, y: x + y
    elif operation == '-':
        result = lambda x, y: x - y
    elif operation == '*':
        result = lambda x, y: x * y
    elif operation == '/':
        result = lambda x, y: x / y
    elif operation == '^':
        result = lambda x, y: x ** y
    else:
        print('Неподдерживаемая операция')
    if result is not None:
        print(result)
