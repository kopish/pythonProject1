# Числа Фибоначчи

# Количество чисел в последовательности
n = 10
# Список чисел Фибоначчи (изначально - две единицы)
fibs = [1, 1]

# Повторяем n - 2 раз, так как два числа уже в списке
for i in range(n - 2):
    # Добавляем сумму двух последних чисел
    fibs.append(fibs[i] + fibs[i + 1])

# Вывод списка на экран
print(fibs)
# Вставка числа 15 под под индексом 1
fibs.insert(1, 15)
# Вывод списка на экран
print(fibs)
# Метод pop(индекс) - удаление элемента по индексу
a = fibs.pop(-3)
print(a)
print(fibs)
# Сортировка по возрастанию
fibs.sort()
print(fibs)
# Добавление нескольких элементов в конец списка
c = (93, 100, 91)
fibs.extend(c)
print(fibs)

