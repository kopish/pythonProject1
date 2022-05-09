string = input('Enter a string: ')
# То же самое, что if string is not None and string != ''

if string:
    print('The string is {}'.format(string))

number = int(input('Enter a number: '))

if number:
    print('Число не равно нулю')
else:
    print('Число равно нулю')
