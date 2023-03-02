my_range = range(10)
my_range1 = range(11, 21)
# Итерирование
for element in my_range:
    print(element)

print()

for element1 in my_range1:
    print(element1)

print()

# Получение доступа к элементам при помощи целочисленных ключей (индексация)
print(my_range[0])
print(my_range[2])
print(my_range[-1])

# Длина последовательности
print('Length:', len(my_range))

my_range = list(range(10))
my_range1 = list(range(10, 21))
my_range2 = my_range + my_range1
print(my_range2)
print('Length:', len(my_range2))
