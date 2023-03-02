x = int(input("Введіть значення х: "))
if -10 <= x <= 10:
    if -5 <= x <= 5:
        y = x ** 2
        print("{} = {} ** 2".format(y, x))
    elif x < -5:
        y = 2 * abs(x) - 1
        print("{} = 2 * |{}| - 1".format(y, x))
    elif x > 5:
        y = 2 * x
        print("{} = 2 * {}".format(y, x))
