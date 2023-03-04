# Напишіть програму, яка зчитує стрічку з консолі та виводить її у
# зворотньому порядку.
while True:
    text = input('Enter a phrase: ')
    print(text[::-1]


# ЧАТ
while True:
    text = input('Enter a phrase: ')
    if text.strip() == '':
        print('Please enter a phrase')
    else:
        print(text[::-1])
        break
