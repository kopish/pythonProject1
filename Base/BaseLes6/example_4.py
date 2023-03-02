# Создание списка
my_list = [1, 3, 6, 10]

# возвести каждый елемент в квадрат, используя списковое включение
list_ = [x ** 2 for x in my_list]

# подобный механизм с генераторами:
# выражения генератора заключены в круглые скобки ()
generator = (x ** 2 for x in my_list)

print(list_)
# print(list(generator))
print(generator)
# [1, 9, 36, 100]
# <generator object <genexpr> at 0x7f5d4eb4bf50>
