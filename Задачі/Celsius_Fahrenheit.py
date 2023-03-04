# Напишіть програму, яка переводить температуру з Цельсія в Фаренгейт або
# навпаки, залежно від вибору користувачf

while True:
    try:
        operator = int(input(f"\nCelsius in Fahrenheit 1\n"
                         f"Fahrenheit in Celsius 2\n"
                             f"Click operation: "))
        if operator == 1:
            num_1 = int(input("Enter the Celsius: "))
            temp_far = num_1 * 1.8 + 32
            print(f'You entered the temperature in Celsius {num_1} '
                  f'Temperature in Fahrenheit {temp_far}')
        elif operator == 2:
            num_2 = int(input("Enter the Fahrenheit: "))
            temp_cls = (num_2 - 32) / 1.8
            print(f'You entered the temperature in Fahrenheit {num_2} '
                  f'Temperature in Celsius {round(temp_cls, 2)}')
    except ValueError:
        print('Invalid input. Please enter an integer.')

