# Факториалом числа n называется число 𝑛! = 1 ∙ 2 ∙ 3 ∙ … ∙ 𝑛.
# Создайте программу, которая вычисляет факториал введённого пользователем числа.
factorial = int(input('Enter the factorial: '))
result = 1
variable = 1
while variable <= factorial:
    result = result * variable
    variable += 1
print("Your factorial:" , factorial,"\n" "Result:", result)