# Список – упорядоченная последовательность определённых значений, которые
# могут повторяться. Количество элементов списка может быть произвольным.
# Для создания списка следует записать его элементы
# через запятую в квадратных скобках.

# int_list – список из четырёх целых чисел
int_list = [1, 2, 3, 5]
print(int_list)
# char_list – список, состоящий из четырёх символов
char_list = ['a', 'c', 'z', 'x']
print(char_list)

# empty_list – пустой список
empty_list = []
print(empty_list)
empty_list1 = list()
print(empty_list1)
n = int(input('Введите число: '))
int_list.append(n)
string = input('Введите букву: ')
char_list.append(string)

print('Список чисел:', int_list)
print('Список символов:', char_list)
print('Пустой список:', empty_list)

int_list.remove(35)
print('Список чисел:', int_list)
del char_list[4]
print('Список символов:', char_list)
char_list[3] = 'm'
print('Список символов:', char_list)

for element in int_list:
    element *= 2
    print(element)
