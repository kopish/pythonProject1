"""
*** Кортеж не изменяется, и можно подумать, что это будет происходить абсолютно всегда.
Но, это не всегда так. В случае наличия изменяемых объёктов внутри кортежа, эти самые объёкты можно модифицировать.
Фактически длинна кортежа не изменилась, но внутренние элементы могли претерпеть внешнее воздействие
"""

my_tuple = ([1, 2], 3, 4)
print('Length:', len(my_tuple))
print(my_tuple)
my_tuple[0].append(15)
print('Length:', len(my_tuple))
print(my_tuple)
my_tuple[0].extend([21, 14, 16, 17, 10])
print('Length:', len(my_tuple))
print(my_tuple)
my_tuple[0].extend('add')
print('Length:', len(my_tuple))
print(my_tuple)

print(len(my_tuple[0]))
