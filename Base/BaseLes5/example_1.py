# Создаем список
my_list = ["One", "piece", "per", "time"]

# Получаем итератор с помощью iter()
my_iter = iter(my_list)

# Итерируем обьект с помощью next()

# Вывод: One
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Вывод: piece
print(my_iter.__next__())

# Вывод: per
print(my_iter.__next__())

# Вывод: time
print(my_iter.__next__())

# Следующий вызов выбросит исключение StopIteration, так как элементы закочнились
next(my_iter)