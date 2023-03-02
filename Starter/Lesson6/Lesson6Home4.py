# вывести чётные значения
def diapazon(a, b):
    while True:
        if b == a:
            return b
        elif b % 2 == 0:
            return b * diapazon(a, b - 1)
        else:
            b -= 1


a = int(input("Number 1: "))
b = int(input("Number 2: "))
print(diapazon(a, b))
