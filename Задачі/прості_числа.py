# Напишіть програму, яка виводить всі прості числа від 1 до N, де N - ціле
# число, яке зчитується з консолі.
# def get_prime_numbers(n):
#     list_numb =[]
#     for i in range(n):
#         list_numb.append(i)
#     print(list_numb)
#
#
# while True:
#     try:
#         value = int(input('Enter an integer: '))
#         break  # вихід з циклу, якщо користувач ввів ціле число
#     except ValueError:
#         print('Invalid input. Please enter an integer.')
#
# get_prime_numbers(value)

# CHAT

def get_prime_numbers(n):
    numbers = list(range(2, n + 1))
    primes = []
    while numbers:
        # Оберіть перше число зі списку та додайте його до списку простих чисел
        p = numbers.pop(0)
        primes.append(p)
        # Видаліть всі числа, що кратні обраному числу зі списку
        numbers = [x for x in numbers if x % p != 0]
    return primes


while True:
    try:
        n = int(input("Enter an integer: "))
        if n < 2:
            print("Please enter an integer greater than or equal to 2.")
        else:
            primes = get_prime_numbers(n)
            print(primes)
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")