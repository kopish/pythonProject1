f1 = 1
f2 = 1

n = int(input("Введіть до якого числа Фібоначчі: "))

while f2 < n:
    print(f2)
    f1, f2 = f2, f1 + f2
    n -= 1