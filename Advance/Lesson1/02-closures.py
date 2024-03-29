﻿"""Пример замыкания"""


def make_closure():
    # Создали переменную
    variable = 42

    # Создали функцию, которая имеет доступ к переменной родительской функции
    def closure():
        return variable

    # Вернули созданную функцию из родительской
    return closure


# Мы уже узнали, что мы можем сохранять функции в обычные перменные. Сохраняем полученную функцию в перменную fn
fn = make_closure()

# Запускам полученную функцию и выводим ее результат
print(fn)
print(fn())
print(type(fn)) # print(type(fn))