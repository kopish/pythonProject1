﻿"""Пример работы с функциями как с объектами первого класса"""

# Создание ссылки на объект
out = print

# Теперь в переменных out и print ссылка на один и тот же алгоритм, 
# поэтому мы можем использовать out так же, как и print 
out('Hello')

# Сохранение ссылок на функции в структуре данных


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

# Используем функции внутри словаря, как обычные переменные
# ВАЖНО: После add и sub не стоят скобки "()", так как наша задача передать их 
# как переменные, а не вызвать


operations = {
    '+': add,
    '-': sub
}

# По ключу словаря получаем полноценную функцию, которую сразу можно вызвать
print(operations['+'](2, 3))
print(operations['-'](2, 3))
out()
out(operations['+'](2, 3))
out(operations['-'](2, 3))
