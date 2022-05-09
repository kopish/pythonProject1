# произведение чисел в диапазоне введённых
def diapazon(a, b):
    if b == a:
        return b
    else:
        return b * diapazon(a, b - 1)


a = int(input("Number 1: "))
b = int(input("Number 2: "))
print(diapazon(a, b))