str1 = 'hel'
str2 = 'lo'
# конкатенация строка
result = str1 + str2

print(result)

# форматирование строк
a = 48
b = 73

message1 = '%d + %d = %d' % (a, b, a + b)
print(message1)

message2 = '{} - {} = {}'.format(a, b, a - b)
print(message2)

message2 = f'{a} - {b} = {a - b}'
print(message2)

# индексация строк
s = 'Hello, World!'

# (вернуться в седьмом уроке)
# индексация начинается с нуля
print(s[0])
# четвёртый (пятый логически) элемент (символ)
print(s[4])
# отрицательные числа – индексация с конца
print(s[-1])

# символы со второго (включительно) по пятый (не включительно)
print(s[2:7])
# то же, но с шагом два
print(s[2:7:2])

print(s[:4:3])
print(s[-1::-1])
