# Числа в десятичной системе счисления
decimal_1 = 8
decimal_2 = 42
decimal_3 = -3
decimal_4 = 25802836572356723058203845293402834028304820938402834023580235777082489436236

print(decimal_1)
print(decimal_2)
print(decimal_3)
print(decimal_4)
# пусто print для переноса строки
print()

# Числа в шестнадцатеричной системе счисления
hexadecimal_1 = 0x9
hexadecimal_2 = 0xA
hexadecimal_3 = 0xFF
hexadecimal_4 = 0x3de

print(hexadecimal_1)
print(hexadecimal_2)
print(hexadecimal_3)
print(hexadecimal_4)
print()

# Число в двоичной системе счисления
bin1 = 0b11101101
print(bin1)
print()

# Число в восьмеричной системе счисления
oct1 = 0o765
print(oct1)
print()

# Построение целого числа из другого значения
string = "15"
number = string
print(number)
print(number + str(5))
# string + 5 -- ошибка
print(int(number) + 5)
print(number * 5)
print(int(number) * 5)
