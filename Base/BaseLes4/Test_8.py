# Для реализации собственного типа исключения необходимо создать класс, являющийся наследником от одного
# из классов исключений.

class NegValException(Exception):
    pass


try:
    val = int(input("input positive number: "))
    if val < 0:
        raise NegValException("Neg val: " + str(val))
    print(val + 10)
except NegValException as e:
    print(e)
