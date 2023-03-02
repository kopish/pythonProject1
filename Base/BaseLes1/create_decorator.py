'''Конструктивно декоратор в Python представляет собой некоторую функцию, аргументом которой является другая функция.
Декоратор предназначен для добавления дополнительного функционала к данной функции без изменения содержимого последней.

Создание декоратора
Предположим у нас есть пара простых функций, вот они:
'''


def first_test():
    print("Test function 1")


def second_test():
    print("Test function 2")
'''Мы хотим дополнить их так, чтобы перед вызовом основного кода функции печаталась строка “Run function”, 
а по окончании – “Stop function”. Сделать это можно двумя способами. Первый – это добавить указанные строки в 
начало в конец каждой функции, но это не очень удобно, т.к. если мы захотим убрать это, нам придется снова
модифицировать тело функции. А если они написаны не нами, либо являются частью общей кодовой базы проекта, 
сделать это будет уже не так просто. Второй вариант – это воспользоваться знаниями  о функциях в Python?”

Создадим вот такую функцию.
'''


def simple_decore(fn):
    def wrapper():
        print("Run function")
        fn()
        print("Stop function")
    return wrapper
# Обернем наши функции в эту оболочку.


first_test_wrapped = simple_decore(first_test)
second_test_wrapped = simple_decore(second_test)
# Функции first_test и second_test остались неизменными.

first_test()
# Test function 1
second_test()
# Test function 2
# Функции first_test_wrapped и second_test_wrapped  обладают функционалом, которого мы добивались.

first_test_wrapped()
'''Run function
Test function 1
Stop function'''
first_test_wrapped()
'''Run function
Test function 1
Stop function'''
# Если необходимо, чтобы так работали функций с именами first_test и second_test, то  можно сделать так.

first_test = first_test_wrapped
second_test = second_test_wrapped
# Давайте проверим это.

first_test()
'''Run function
Test function 1
Stop function'''
second_test()
'''Run function
Test function 2
Stop function'''
# То, что мы только что сделали и является реализацией идеи декоратора. Но вместо строк:
'''
def first_test():
    print("Test function 1")
first_test_wrapped = simple_decore(first_test)
first_test = first_test_wrapped 
# Можно написать вот так:
'''
@simple_decore
# декоратор функции
def first_test():
    print("Test function 1")
