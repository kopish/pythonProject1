'''Создайте функцию infinite(lst, tries), которая будет проходиться по элементам списка lst (целые числа) заданное
количество раз (tries) циклически. Один раз - один элемент списка.
После вывода последнего значения последовательности процедура начнется с самого начала.

Например, если в списке 2 элемента, а функция получила значение 3, то сначала выведется первый объект,
потом последний, а потом опять первый.
Результат работы функции представьте в виде строки, состоящей из tries количества символов.'''

'''Для решения задачи нужно использовать функцию cycle() из модуля itertools. Она перебирает последовательность 
циклически, а по мере достижения последнего элемента начинает заново.'''

from itertools import cycle


def infinite(lst, iterations):
    result = ''
    iter_lst = cycle(lst)
    if lst:
        for symbol in range(iterations):
            result += str(next(iter_lst))
    return result


# Тесты
print(infinite([2, 5, 8, 13, 21, 45, 145, 210, 233], 7))
print(infinite(['/', r'\''], 70))
print(infinite([], 1000))
print(infinite([7], 4))
