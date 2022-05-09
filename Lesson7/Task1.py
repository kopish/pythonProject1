my_list = [5, 7, 1, 5, 8, 7, 1, 0, 7, -23, 15]

# Копирование списка - метод copy()
my_list1 = my_list.copy()

# Получение порядкового номера первого элемента со значением 7 в диапазоне со 2го индекса до 8-го:
print(my_list.index(7, 2, 8))
# Подсчитываем количество 5-ок в списке:
print(my_list.count(5))

# Cортировка списка по возрастанию:
my_list.sort()
print(my_list)
# Cортировка списка по убыванию:
my_list.reverse()
print(my_list)

print(my_list1)
# Очищаем список my_list
my_list.clear()
print(my_list)

char_list = ["a", "e", "i", "o", "u", "y"]
str_list = "; ".join(char_list)
print("Строка гласных:", str_list)
