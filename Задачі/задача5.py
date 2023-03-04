# Напишіть програму, яка знаходить суму чисел від 1 до N, де N - ціле число,
# яке зчитується з консолі.
# відповідь на задачу 5 вірна?
def stairs(n):
    if n == 1:
        return 1
    return stairs(n - 1) + n


while True:
    try:
        number = int(input(f'Enter a number: '))
    except ValueError:
        print('Invalid input. Please enter an integer.')
    break

print(stairs(number))
