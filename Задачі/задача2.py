# Напишіть програму, яка обчислює середнє арифметичне двох чисел,
# які зчитуються з консолі.

while True:
    try:
        value1 = float(input('Enter the first integer : '))
        value2 = float(input('Enter the second integer: '))
        listnumbers = [value1, value2]
        break  # вихід з циклу, якщо користувач ввів число
    except ValueError:
        print('Invalid input. Please enter an integer.')

print(f'The arithmetic mean of your numbers:'
    f' {sum(listnumbers) / len(listnumbers)}')

# ЧАТ
# numbers = []
# while True:
#     value = input("Enter a number, or 'stop' to finish: ")
#     if value.lower() in ['stop', 's']:
#         break
#     try:
#         numbers.append(float(value))
#     except ValueError:
#         print("Invalid input. Please enter a number or 'stop' to finish.")
#
# if len(numbers) == 0:
#     print("No numbers entered.")
# else:
#     average = sum(numbers) / len(numbers)
#     print(f"The average of {len(numbers)} numbers is {average}")