string = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."

# Итерирование
for character in string:
    print(character)

# Получение доступа к элементам при помощи целочисленных ключей (индексация)
print(string[0])
print(string[2])
print(string[-1])

print(string[15::5])
print(string[-15::5])

# Длина последовательности
print('Length:', len(string))

print('Min element in string:', min(string))
print('Max element in string:', max(string))

string2 = string.find("a")
print('New string is: ', ((string + str(string2) + " ") * 3))
