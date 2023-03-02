# Разница между discard() и remove()

# Создание множества
my_set = {1, 3, 4, 5, 6}
print(my_set)

# Исключение элемента
# Вывод: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# Удаление элемента
# Вывод: {1, 3, 5}
my_set.remove(6)
print(my_set)

# Исключние элемента,
# которого нет в множестве
# Вывод: {1, 3, 5}
my_set.discard(2)
print(my_set)

# Удаление элемента
# которого нет в множестве
# Вывод: KeyError
# my_set.remove(2)

my_set.clear()
print(my_set)
