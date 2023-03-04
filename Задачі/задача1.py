# Напишіть програму, яка зчитує ціле число з консолі та виводить на екран,
# чи воно є парним чи непарним.

while True:
    value = int(input('Enter an integer: '))
    if value % 2 == 0:
        print(f'{value} is an even number')
    else:
        print(f'this number {value} is not even')

# ЧАТ
# while True:
#     try:
#         value = int(input('Enter an integer: '))
#         break  # вихід з циклу, якщо користувач ввів ціле число
#     except ValueError:
#         print('Invalid input. Please enter an integer.')
#
# if value % 2 == 0:
#     print(f'{value} is an even number')
# else:
#     print(f'{value} is not an even number')
