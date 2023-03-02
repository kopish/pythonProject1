# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать
# данное исключение, если пользователь введёт определённое значение, и
# перехватите это исключение при вызове функции.
class PozValException(Exception):
    pass


try:
    value = int(input("input negative number: "))
    if value > 0:
        raise PozValException("Neg val: " + str(value))
    print(value - 10)
except PozValException as e:
    print(e)
