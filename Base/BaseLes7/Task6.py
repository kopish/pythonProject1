# Создание кортежей
my_tuple = ()
print(my_tuple)

my_tuple1 = (1,)
print(my_tuple1)

my_tuple2 = 1,
print(my_tuple2)

my_tuple3 = (1, 2, 'a string')
print(my_tuple3)

my_tuple4 = 1, 2, 'a string'
print(my_tuple4)

my_tuple5 = tuple(range(8))
print(my_tuple5)
# Количество двоек в кортеже my_tuple5
print(my_tuple5.count(2))
my_tuple6 = (1, 2, 2, 3, 1, 2, 4, 3, 2, 2.0)
print(my_tuple6)
# Количество двоек в кортеже my_tuple6
print(my_tuple6.count(2))
# получение индекса (позиции) элемента в кортеже
print('Индекс =', my_tuple6.index(2))
# получние индекса (позиции) несуществующего элемента в кортеже - ValueError
# print('Индекс =', my_tuple6.index(5))
print(my_tuple6.index(2, 2))
print(my_tuple6.index(2, 4, 6))
