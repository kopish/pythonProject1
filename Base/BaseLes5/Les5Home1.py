# Реализуйте цикл, который будет перебирать все значения итерабельного
# объекта iterable.
iterable = [1, 5, 8, 9]
my_iter = iter(iterable)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

for i in iterable:
    print(i)

